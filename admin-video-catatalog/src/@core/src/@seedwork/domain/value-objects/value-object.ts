import { deepFreeze } from '@core/src/@seedwork/domain';

export abstract class ValueObject<Value = any> {
  protected readonly _value: Value;

  constructor(value: Value) {
    this._value = deepFreeze<Value>(value);
  }

  get value(): Value {
    return this._value;
  }

  toString = (): string => {
    if (typeof this._value !== 'object' || this._value === null) {
      try {
        return this._value.toString();
      } catch (err) {
        return this._value + '';
      }
    }

    const valueStr = this._value.toString();
    return valueStr === '[object Object]'
      ? JSON.stringify(this._value)
      : valueStr;
  };
}
