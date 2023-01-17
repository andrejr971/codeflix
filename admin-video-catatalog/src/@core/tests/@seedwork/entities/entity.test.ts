import { UniqueEntityId } from '@core/src/@seedwork/domain/value-objects/unique-entity-id.vo';
import { Entity } from '@core/src/@seedwork/entities/entity';

class StubEntity extends Entity<{ prop1: string; prop2: number }> {}

describe('Entity unit test', () => {
  it('should set props and id', () => {
    const arrange = {
      prop1: 'value',
      prop2: 20,
    };
    const entity = new StubEntity(arrange);
    expect(entity.props).toStrictEqual(arrange);
    expect(entity.uniqueEntityId).toBeInstanceOf(UniqueEntityId);
    expect(entity.id).not.toBeNull();
  });

  it('should accepted a valid uuid', () => {
    const arrange = {
      prop1: 'value',
      prop2: 20,
    };
    const uniqueEntityId = new UniqueEntityId();
    const entity = new StubEntity(arrange, uniqueEntityId);
    expect(entity.uniqueEntityId).toBeInstanceOf(UniqueEntityId);
    expect(entity.id).toBe(uniqueEntityId.value);
  });

  it('should convert a entity to a Javascript object', () => {
    const arrange = {
      prop1: 'value',
      prop2: 20,
    };
    const uniqueEntityId = new UniqueEntityId();
    const entity = new StubEntity(arrange, uniqueEntityId);
    expect(entity.toJson()).toStrictEqual({
      id: uniqueEntityId.value,
      ...arrange,
    });
  });
});
