import {v4 as uuid, validate as uuidValidate} from 'uuid';

import {ValueObject} from '../value-object';

export class Uuid extends ValueObject {
  readonly id: string;

  constructor(id?: string) {
    super();
    this.id = id || this.generate();
    this.validate();
  }

  generate(): string {
    return uuid();
  }

  private validate() {
    const isValidateUuid = uuidValidate(this.id);
    if (!isValidateUuid) {
      throw new InvalidUuidError();
    }
  }

  toString(): string {
    return this.id;
  }
}

export class InvalidUuidError extends Error {
  constructor(message: string = 'ID must be a valid UUID') {
    super(message);
    this.name = 'InvalidUuidError';
  }
}
