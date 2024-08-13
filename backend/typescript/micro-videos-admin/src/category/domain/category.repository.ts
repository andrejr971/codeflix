import {IRepository} from '@/shared/domain/repository/repository.interface';
import {Uuid} from '@/shared/domain/value-objects/uuid.vo';

import {Category} from './category.entity';

export interface ICategoryRepository extends IRepository<Category, Uuid> {}

export class CategoryRepository implements ICategoryRepository {
  insert(entity: Category): Promise<void> {
    throw new Error('Method not implemented.');
  }

  bulkInsert(entities: Category[]): Promise<void> {
    throw new Error('Method not implemented.');
  }

  update(entity: Category): Promise<void> {
    throw new Error('Method not implemented.');
  }

  delete(entity: Category): Promise<void> {
    throw new Error('Method not implemented.');
  }

  findById(id: Uuid): Promise<Category> {
    throw new Error('Method not implemented.');
  }

  findAll(): Promise<Category[]> {
    throw new Error('Method not implemented.');
  }

  getEntityName(): new (...args: any[]) => Category {
    throw new Error('Method not implemented.');
  }
}
