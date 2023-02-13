import { CategoryValidator } from '#category/domain';

export class CategoryValidatorFactory {
  static create() {
    return new CategoryValidator();
  }
}
