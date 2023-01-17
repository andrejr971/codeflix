import { UniqueEntityId } from '@core/src/@seedwork/domain/value-objects/unique-entity-id.vo';
import { InvalidUuidError } from '@core/src/@seedwork/errors/invalid-uuid.error';

let validateSpy: any;
describe('UniqueentityId Unit Test', () => {
  beforeEach(() => {
    validateSpy = jest.spyOn(UniqueEntityId.prototype as any, 'validate');
  });

  it('should throw error when uuid is invalid', () => {
    expect(() => new UniqueEntityId('fake')).toThrow(new InvalidUuidError());
    expect(validateSpy).toHaveBeenCalled();
  });

  it('should be validate uuid', () => {
    const uuid = 'fa30ab15-7d84-4bc5-9c9a-1f660ea4e20a';
    const uuidVo = new UniqueEntityId('fa30ab15-7d84-4bc5-9c9a-1f660ea4e20a');

    expect(() => uuidVo).not.toThrow(new InvalidUuidError());
    expect(uuidVo.id).toEqual(uuid);
    expect(validateSpy).toHaveBeenCalled();
  });

  it('should be generate new id', () => {
    const uuid = new UniqueEntityId();

    expect(() => uuid).not.toThrow(new InvalidUuidError());
    expect(uuid).toHaveProperty('id');
    expect(validateSpy).toHaveBeenCalled();
  });
});
