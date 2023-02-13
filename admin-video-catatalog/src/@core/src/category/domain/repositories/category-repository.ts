import {
  SearchableRepositoryInterface,
  SearchParams,
  SearchResult,
} from '#seedwork/domain';
import { Category } from '#category/domain';

export namespace CategoryRepository {
  export type Filter = string;

  export class Params extends SearchParams<Filter> {}

  export class Response extends SearchResult<Category, Filter> {}

  export interface Repository
    extends SearchableRepositoryInterface<Category, Filter, Params, Response> {}
}
