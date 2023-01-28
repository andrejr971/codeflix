import { FieldsErrors } from '../validators/validator-fields-interface';

declare global {
  declare namespace jest {
    interface Matchers<R> {
      containsErrorMessages: (received: FieldsErrors) => R;
    }
  }
}
