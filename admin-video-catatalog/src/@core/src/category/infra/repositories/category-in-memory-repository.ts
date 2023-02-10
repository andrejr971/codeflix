import { InMemorySearchableRepository } from '@core/src/@seedwork/domain';
import { Category } from '../../domain/entities/category';
import { CategoryRepository } from '../../domain/repositories/category-repository';

export class CategoryInMemoryRepository
  extends InMemorySearchableRepository<Category>
  implements CategoryRepository {}
