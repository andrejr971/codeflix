import { Uuid } from "../../../shared/domain/value-objects/uuid.vo";
import { InMemoryRepository } from "../../../shared/infra/db/in-memory/in-memory.repository";
import { Category } from "../../domain/category.entity";

export class CategoryInMemoryRepositoty extends InMemoryRepository<Category, Uuid> {
  getEntity(): new (...args: any[]) => Category {
    return Category;
  }
}