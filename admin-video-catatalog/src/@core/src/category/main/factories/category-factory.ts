import { CategoryValidator } from '@core/src/category/domain';

export class CategoryValidatorFactory {
  static create() {
    return new CategoryValidator();
  }
}
