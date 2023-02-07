import { Entity, UniqueEntityId } from '@core/src/@seedwork/domain';

export interface RepositoryInterface<T extends Entity> {
  create(entity: T): Promise<void>;
  findById(id: string | UniqueEntityId): Promise<T>;
  findAll(): Promise<T[]>;
  update(entity: T): Promise<void>;
  delete(id: string | UniqueEntityId): Promise<void>;
}
