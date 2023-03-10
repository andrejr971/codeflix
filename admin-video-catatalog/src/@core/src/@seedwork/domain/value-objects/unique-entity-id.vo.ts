import { v4 as uuidV4, validate as uuidValidate } from 'uuid';
import { InvalidUuidError } from '@core/src/@seedwork/domain';
import { ValueObject } from './value-object';

export class UniqueEntityId extends ValueObject<string> {
  constructor(readonly id?: string) {
    super(id || uuidV4());
    this.validate();
  }

  private validate() {
    const isValid = uuidValidate(this._value);

    if (!isValid) throw new InvalidUuidError();
  }
}
