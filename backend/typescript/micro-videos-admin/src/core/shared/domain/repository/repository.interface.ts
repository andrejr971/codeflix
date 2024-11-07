import {Entity} from '../entity';
import {ValueObject} from '../value-object';
import type {SearchParams} from './search-params';
import type {SearchResult} from './search-result';

export interface IRepository<T extends Entity, EntityId extends ValueObject> {
  insert(entity: T): Promise<void>;
  bulkInsert(entities: T[]): Promise<void>;
  update(entity: T): Promise<void>;
  delete(id: EntityId): Promise<void>;

  findById(id: EntityId): Promise<T | null>;
  findAll(): Promise<T[]>;

  getEntity(): new (...args: any[]) => T;
}

export interface ISearchableRepository<
  E extends Entity,
  EntityId extends ValueObject,
  Filter = string,
  SearchInput = SearchParams<Filter>,
  SearchOutput = SearchResult,
> extends IRepository<E, EntityId> {
  sortableFields: string[];
  search(props: SearchInput): Promise<SearchOutput>;
}
