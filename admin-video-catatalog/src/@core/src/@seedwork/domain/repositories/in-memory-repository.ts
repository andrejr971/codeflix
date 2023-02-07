import { Entity } from '../entities';
import { NotFoundError } from '../errors';
import { UniqueEntityId } from '../value-objects';
import { RepositoryInterface } from './respository';

export abstract class InMemoryRepository<T extends Entity>
  implements RepositoryInterface<T>
{
  public items: T[] = [];

  async create(entity: T): Promise<void> {
    this.items.push(entity);
  }

  async findById(id: string | UniqueEntityId): Promise<T> {
    return this._get(id);
  }

  async findAll(): Promise<T[]> {
    return this.items;
  }

  async update(entity: T): Promise<void> {
    await this._get(entity.id);
    const indexFound = this.items.findIndex((item) => item.id === entity.id);
    this.items[indexFound] = entity;
  }

  async delete(id: string | UniqueEntityId): Promise<void> {
    await this._get(`${id}`);
    const indexFound = this.items.findIndex((item) => item.id === `${id}`);
    this.items.splice(indexFound, 1);
  }

  protected async _get(id: string | UniqueEntityId): Promise<T> {
    const item = this.items.find((item) => item.id === `${id}`);
    if (!item) throw new NotFoundError(`Not found using ID ${id}`);
    return item;
  }
}
