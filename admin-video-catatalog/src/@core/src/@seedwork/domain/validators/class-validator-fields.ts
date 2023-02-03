import { validateSync, ValidationError } from 'class-validator';

import {
  FieldsErrors,
  ValidatorFieldsInterface,
} from './validator-fields-interface';

export abstract class ClassValidatorFields<T>
  implements ValidatorFieldsInterface<T>
{
  errors: FieldsErrors = null;
  validatedData: T = null;

  validate(data: any) {
    const errors: ValidationError[] = validateSync(data);

    if (errors.length) {
      this.errors = {};
      errors.forEach((error) => {
        this.errors[error.property] = Object.values(error.constraints);
      });
    } else {
      this.validatedData = data;
    }

    return !errors.length;
  }
}
