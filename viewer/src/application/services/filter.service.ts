import { ArchitectureGraph } from '../../domain/models/architecture-graph';
import { FilterOptions, GraphFilterService } from '../../domain/services/graph-filter.service';
import { FilterGraphUseCase } from '../../ports/inbound/use-cases';

export class FilterService implements FilterGraphUseCase {
  constructor(private readonly filterService: GraphFilterService) {}

  public execute(graph: ArchitectureGraph, options: FilterOptions): ArchitectureGraph {
    return this.filterService.filter(graph, options);
  }
}
