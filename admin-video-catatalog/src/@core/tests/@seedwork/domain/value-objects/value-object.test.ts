import { ValueObject } from '@core/src/@seedwork/domain/value-objects/value-object';

class StubValueObject extends ValueObject {}

describe('Value object unit test', () => {
  it('should set value', () => {
    let vo = new StubValueObject('string value');
    expect(vo.value).toBe('string value');

    vo = new StubValueObject({ prop1: 'value1' });
    expect(vo.value).toStrictEqual({
      prop1: 'value1',
    });
  });

  it('should convert to string', () => {
    const date = new Date();

    let arrange = [
      { received: '', expected: '' },
      { received: 'fake test', expected: 'fake test' },
      { received: 0, expected: '0' },
      { received: 1, expected: '1' },
      { received: 5.6, expected: '5.6' },
      { received: true, expected: 'true' },
      { received: false, expected: 'false' },
      { received: date, expected: date.toString() },
      {
        received: { prop1: 'value1' },
        expected: JSON.stringify({ prop1: 'value1' }),
      },
    ];

    arrange.forEach((value) => {
      const vo = new StubValueObject(value.received);
      expect(`${vo}`).toBe(value.expected);
    });
  });

  it('immutable', () => {
    const vo = new StubValueObject({
      prop1: 'value',
      nested: { prop2: new Date() },
    });
    expect(typeof vo).toBe('object');
    expect(() => {
      vo['_value'].nested.prop2 = 'mudou';
    }).toThrow(
      "Cannot assign to read only property 'prop2' of object '#<Object>'",
    );
  });
});
