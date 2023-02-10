import {
  SearchableRepositoryInterface,
  SearchParams,
  SearchResult,
} from '@core/src/@seedwork/domain';
import { Category } from '../entities/category';

export namespace CategoryRepository {
  export type Filter = string;

  export class Params extends SearchParams<Filter> {}

  export class Result extends SearchResult<Category, Filter> {}

  export interface Repository
    extends SearchableRepositoryInterface<
      Category,
      Filter,
      SearchParams,
      SearchResult
    > {}
}
