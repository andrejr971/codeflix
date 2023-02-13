import {
  SearchableRepositoryInterface,
  SearchParams,
  SearchResult,
} from '@core/src/@seedwork/domain';
import { Category } from '@core/src/category/domain';

export namespace CategoryRepository {
  export type Filter = string;

  export class Params extends SearchParams<Filter> {}

  export class Response extends SearchResult<Category, Filter> {}

  export interface Repository
    extends SearchableRepositoryInterface<Category, Filter, Params, Response> {}
}
