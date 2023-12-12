import { Entity } from "../../../domain/entity";
import { NotFoundError } from "../../../domain/errors/not-found.error";
import { IRepository } from "../../../domain/repository/repository-interface";
import { ValueObject } from "../../../domain/value-object";

export abstract class InMemoryRepository<T extends Entity, EntityId extends ValueObject> implements IRepository<T, EntityId> {
  items: T[] = []

  async insert(entity: T): Promise<void> {
    this.items.push(entity);
  }

  async bulkInsert(entities: T[]): Promise<void> {
    this.items.push(...entities);
  }

  async update(entity: T): Promise<void> {
    const indexFound = this.items.findIndex((item) =>
      item.entity_id.equals(entity.entity_id)
    );
    if (indexFound === -1) {
      throw new NotFoundError(entity.entity_id, this.getEntity());
    }
    this.items[indexFound] = entity;
  }

  async delete(entity_id: EntityId): Promise<void> {
    const indexFound = this.items.findIndex((item) =>
      item.entity_id.equals(entity_id)
    );
    if (indexFound === -1) {
      throw new NotFoundError(entity_id, this.getEntity());
    }
    this.items.splice(indexFound, 1);
  }

  async findById(entity_id: EntityId): Promise<T> {
    const item = this.items.find((item) => item.entity_id.equals(entity_id));
    return typeof item === "undefined" ? null : item;
  }

  async findAll(): Promise<T[]> {
    return this.items;
  }

  abstract getEntity(): new (...args: any[]) => T;
}