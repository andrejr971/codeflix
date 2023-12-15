import { Entity } from "../entity";
import { ValueObject } from "../value-object";
import { SearchParams } from "./search-params";
import { SearchResult } from "./search-result";

export interface IRepository<T extends Entity, EntityId extends ValueObject> {
  insert(entity: T): Promise<void>;
  bulkInsert(entities: T[]): Promise<void>;
  update(entity: T): Promise<void>;
  delete(entity_id: EntityId): Promise<void>;

  findById(entity_id: EntityId): Promise<T | null>;
  findAll(): Promise<T[]>;

  getEntity(): new (...args: any[]) => T;
}

export interface ISearchableRepository<
  T extends Entity, 
  EntityId extends ValueObject, 
  SearchInput = SearchParams<''>, 
  SearchOutput = SearchResult
> extends IRepository<T, EntityId>{
  sortableFields: string[];
  search(props: SearchInput): Promise<SearchOutput>;
}