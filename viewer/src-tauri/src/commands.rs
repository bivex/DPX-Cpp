use std::path::{Path, PathBuf};
use std::process::Command;
use serde_json::Value;

/// Locate uv or pattern-detector executable
fn find_uv_executable() -> Option<PathBuf> {
    let candidates = [
        "/Users/password9090/.local/bin/uv",
        "/opt/homebrew/bin/uv",
        "/usr/local/bin/uv",
    ];

    for path_str in &candidates {
        let p = Path::new(path_str);
        if p.exists() {
            return Some(p.to_path_buf());
        }
    }

    // Try finding via `which uv`
    if let Ok(output) = Command::new("which").arg("uv").output() {
        if output.status.success() {
            let path_str = String::from_utf8_lossy(&output.stdout).trim().to_string();
            if !path_str.is_empty() {
                return Some(PathBuf::from(path_str));
            }
        }
    }

    Some(PathBuf::from("uv"))
}

/// Find DPX-Cpp workspace root directory (containing pyproject.toml)
fn find_workspace_root() -> PathBuf {
    let mut current = std::env::current_dir().unwrap_or_else(|_| PathBuf::from("."));
    for _ in 0..6 {
        if current.join("pyproject.toml").exists() && current.join("src").join("pattern_detector").exists() {
            return current;
        }
        if let Some(parent) = current.parent() {
            current = parent.to_path_buf();
        } else {
            break;
        }
    }
    PathBuf::from("/Volumes/External/Code/DPX-Cpp")
}

#[tauri::command]
pub fn scan_project(project_path: String, min_confidence: Option<f64>) -> Result<Value, String> {
    let uv = find_uv_executable().ok_or_else(|| "Could not locate 'uv' binary".to_string())?;
    let workspace = find_workspace_root();

    let tmp_dir = std::env::temp_dir();
    let tmp_json = tmp_dir.join(format!("dpx_scan_{}.json", std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_millis()));

    let conf_str = min_confidence.unwrap_or(0.0).to_string();

    let mut cmd = Command::new(&uv);
    cmd.current_dir(&workspace)
        .arg("run")
        .arg("pattern-detector")
        .arg("scan")
        .arg(&project_path)
        .arg("--min-confidence")
        .arg(&conf_str)
        .arg("--json")
        .arg(&tmp_json);

    // Set PATH environment variable so python and uv find tools
    if let Ok(path) = std::env::var("PATH") {
        cmd.env("PATH", format!("/Users/password9090/.local/bin:/opt/homebrew/bin:/usr/local/bin:{}", path));
    }

    let output = cmd.output().map_err(|e| format!("Failed to execute scan: {}", e))?;

    if !tmp_json.exists() {
        let err_text = String::from_utf8_lossy(&output.stderr);
        let out_text = String::from_utf8_lossy(&output.stdout);
        return Err(format!("Scan failed or produced no output JSON.\nStdout: {}\nStderr: {}", out_text, err_text));
    }

    let content = std::fs::read_to_string(&tmp_json).map_err(|e| format!("Failed to read scan output: {}", e))?;
    let _ = std::fs::remove_file(&tmp_json);

    serde_json::from_str(&content).map_err(|e| format!("Invalid JSON output from scan: {}", e))
}

#[tauri::command]
pub fn trace_dataflow_all(project_path: String) -> Result<Value, String> {
    let uv = find_uv_executable().ok_or_else(|| "Could not locate 'uv' binary".to_string())?;
    let workspace = find_workspace_root();

    let tmp_dir = std::env::temp_dir();
    let tmp_json = tmp_dir.join(format!("dpx_df_all_{}.json", std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_millis()));

    let mut cmd = Command::new(&uv);
    cmd.current_dir(&workspace)
        .arg("run")
        .arg("pattern-detector")
        .arg("dataflow")
        .arg("--all")
        .arg("--path")
        .arg(&project_path)
        .arg("--json")
        .arg(&tmp_json);

    if let Ok(path) = std::env::var("PATH") {
        cmd.env("PATH", format!("/Users/password9090/.local/bin:/opt/homebrew/bin:/usr/local/bin:{}", path));
    }

    let output = cmd.output().map_err(|e| format!("Failed to execute dataflow: {}", e))?;

    if !tmp_json.exists() {
        let err_text = String::from_utf8_lossy(&output.stderr);
        return Err(format!("Dataflow failed.\nStderr: {}", err_text));
    }

    let content = std::fs::read_to_string(&tmp_json).map_err(|e| format!("Failed to read dataflow output: {}", e))?;
    let _ = std::fs::remove_file(&tmp_json);

    serde_json::from_str(&content).map_err(|e| format!("Invalid JSON output from dataflow: {}", e))
}

#[tauri::command]
pub fn trace_dataflow_target(
    project_path: String,
    target: String,
    direction: Option<String>,
    variant: Option<String>,
) -> Result<Value, String> {
    let uv = find_uv_executable().ok_or_else(|| "Could not locate 'uv' binary".to_string())?;
    let workspace = find_workspace_root();

    let tmp_dir = std::env::temp_dir();
    let tmp_json = tmp_dir.join(format!("dpx_df_target_{}.json", std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_millis()));

    let dir = direction.unwrap_or_else(|| "out".to_string());
    let var = variant.unwrap_or_else(|| "simplified".to_string());

    let mut cmd = Command::new(&uv);
    cmd.current_dir(&workspace)
        .arg("run")
        .arg("pattern-detector")
        .arg("dataflow")
        .arg(&target)
        .arg("--path")
        .arg(&project_path)
        .arg("--direction")
        .arg(&dir)
        .arg("--variant")
        .arg(&var)
        .arg("--json")
        .arg(&tmp_json);

    if let Ok(path) = std::env::var("PATH") {
        cmd.env("PATH", format!("/Users/password9090/.local/bin:/opt/homebrew/bin:/usr/local/bin:{}", path));
    }

    let output = cmd.output().map_err(|e| format!("Failed to execute dataflow target: {}", e))?;

    if !tmp_json.exists() {
        let err_text = String::from_utf8_lossy(&output.stderr);
        return Err(format!("Dataflow target failed.\nStderr: {}", err_text));
    }

    let content = std::fs::read_to_string(&tmp_json).map_err(|e| format!("Failed to read dataflow target output: {}", e))?;
    let _ = std::fs::remove_file(&tmp_json);

    serde_json::from_str(&content).map_err(|e| format!("Invalid JSON output from dataflow target: {}", e))
}

#[tauri::command]
pub fn read_source_file(file_path: String) -> Result<String, String> {
    let path = Path::new(&file_path);
    if !path.exists() {
        return Err(format!("File does not exist: {}", file_path));
    }
    std::fs::read_to_string(path).map_err(|e| format!("Failed to read file: {}", e))
}

#[tauri::command]
pub fn load_json_file(file_path: String) -> Result<Value, String> {
    let path = Path::new(&file_path);
    if !path.exists() {
        return Err(format!("File does not exist: {}", file_path));
    }
    let content = std::fs::read_to_string(path).map_err(|e| format!("Failed to read JSON file: {}", e))?;
    serde_json::from_str(&content).map_err(|e| format!("Invalid JSON format: {}", e))
}
