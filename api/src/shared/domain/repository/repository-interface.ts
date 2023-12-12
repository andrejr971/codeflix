import { Entity } from "../enitity";
import { ValueObject } from "../value-object";

export interface IRepository<T extends Entity, EntityId extends ValueObject> {
  insert(entity: T): Promise<void>;
  bulkInsert(entities: T[]): Promise<void>;
  update(entity: T): Promise<void>;
  delete(entity_id: EntityId): Promise<void>;

  findById(entity_id: EntityId): Promise<T | null>;
  findAll(): Promise<T[]>;

  getEntity: new (...args: any[]) => T
}