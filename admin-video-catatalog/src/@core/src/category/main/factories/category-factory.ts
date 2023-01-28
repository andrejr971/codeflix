import { CategoryValidator } from '../../domain/validators/category-validator';

export class CategoryValidatorFactory {
  static create() {
    return new CategoryValidator();
  }
}
