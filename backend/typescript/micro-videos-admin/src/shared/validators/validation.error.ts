import {FieldsErrors} from './validator-fields-interface';

export class ValidationError extends Error {}

export class EntityValidationError extends Error {
  // eslint-disable-next-line n/handle-callback-err
  constructor(
    public error: FieldsErrors,
    message = 'Validation Error',
  ) {
    super(message);
  }

  count() {
    return Object.keys(this.error).length;
  }
}
