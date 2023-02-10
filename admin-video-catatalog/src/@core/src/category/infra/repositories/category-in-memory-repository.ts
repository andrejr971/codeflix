import {
  InMemorySearchableRepository,
  SortDirection,
} from '@core/src/@seedwork/domain';
import { Category } from '../../domain/entities/category';
import { CategoryRepository } from '../../domain/repositories/category-repository';

export class CategoryInMemoryRepository
  extends InMemorySearchableRepository<Category>
  implements CategoryRepository.Repository
{
  sortableFields: string[] = ['name', 'created_at'];

  protected async applyFilter(
    data: Category[],
    filter: CategoryRepository.Filter,
  ): Promise<Category[]> {
    if (!filter) {
      return data;
    }

    return data.filter((i) => {
      return i.props.name.toLowerCase().includes(filter.toLowerCase());
    });
  }

  protected async applySort(
    items: Category[],
    sort: string | null,
    sort_dir: SortDirection | null,
  ): Promise<Category[]> {
    return !sort
      ? super.applySort(items, 'created_at', 'desc')
      : super.applySort(items, sort, sort_dir);
  }
}
