import { deepFreeze } from '@core/src/@seedwork/utils/object';

describe('Object unite test', () => {
  it('should not freeze a scalar value', () => {
    const string = deepFreeze('a');
    expect(typeof string).toBe('string');

    const boolean = deepFreeze(true);
    expect(typeof boolean).toBe('boolean');

    const number = deepFreeze(5);
    expect(typeof number).toBe('number');
  });

  it('should be a immutable object', () => {
    const object = deepFreeze({
      prop1: 'value1',
      deep: {
        prop2: 'value2',
        prop3: new Date(),
      },
    });
    expect(typeof object).toBe('object');
    expect(() => {
      object['deep'].prop2 = 'mudou';
    }).toThrow(
      "Cannot assign to read only property 'prop2' of object '#<Object>'",
    );
    expect(object['deep'].prop3).toBeInstanceOf(Date);
  });
});
