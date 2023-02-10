import { SearchableRepositoryInterface } from '@core/src/@seedwork/domain';
import { Category } from '../entities/category';

export interface CategoryRepository
  extends SearchableRepositoryInterface<Category, any, any> {}
