import {
  Entity,
  InMemoryRepository,
  NotFoundError,
  UniqueEntityId,
} from '@core/src/@seedwork/domain';

type StubEntityProps = {
  name: string;
  price: number;
};

class StubEntity extends Entity<StubEntityProps> {}

class StubInMemoryRepository extends InMemoryRepository<StubEntity> {}

describe('InMemoryRepository Unit Tests', () => {
  let repository: StubInMemoryRepository;

  beforeEach(() => {
    repository = new StubInMemoryRepository();
  });

  it('should create a new entity', async () => {
    const entity = new StubEntity({ name: 'name', price: 2.99 });
    await repository.create(entity);

    expect(entity.toJson()).toEqual(repository.data[0].toJson());
  });

  it('should throws error when entity not found', () => {
    expect(repository.findById('faker_id')).rejects.toThrow(
      new NotFoundError(`Not found using ID faker_id`),
    );

    expect(
      repository.findById(
        new UniqueEntityId('d80623d3-7f1b-47a9-94ce-1ccddd512c3c'),
      ),
    ).rejects.toThrow(
      new NotFoundError(
        `Not found using ID d80623d3-7f1b-47a9-94ce-1ccddd512c3c`,
      ),
    );
  });

  it('should finds a entity by id', async () => {
    const entity = new StubEntity({ name: 'name value', price: 5 });
    await repository.create(entity);

    let entityFound = await repository.findById(entity.id);
    expect(entity.toJson()).toStrictEqual(entityFound.toJson());

    entityFound = await repository.findById(entity.uniqueEntityId);
    expect(entity.toJson()).toStrictEqual(entityFound.toJson());
  });

  it('should returns all entities', async () => {
    const entity = new StubEntity({ name: 'name value', price: 5 });
    await repository.create(entity);

    const entities = await repository.findAll();

    expect(entities).toStrictEqual([entity]);
  });

  it('should throws error on update when entity not found', () => {
    const entity = new StubEntity({ name: 'name value', price: 5 });
    expect(repository.update(entity)).rejects.toThrow(
      new NotFoundError(`Not found using ID ${entity.id}`),
    );
  });

  it('should updates an entity', async () => {
    const entity = new StubEntity({ name: 'name value', price: 5 });
    await repository.create(entity);

    const entityUpdated = new StubEntity(
      { name: 'updated', price: 1 },
      entity.uniqueEntityId,
    );
    await repository.update(entityUpdated);
    expect(entityUpdated.toJson()).toStrictEqual(repository.data[0].toJson());
  });

  it('should throws error on delete when entity not found', () => {
    expect(repository.delete('fake id')).rejects.toThrow(
      new NotFoundError('Not found using ID fake id'),
    );

    expect(
      repository.delete(
        new UniqueEntityId('9366b7dc-2d71-4799-b91c-c64adb205104'),
      ),
    ).rejects.toThrow(
      new NotFoundError(
        `Not found using ID 9366b7dc-2d71-4799-b91c-c64adb205104`,
      ),
    );
  });

  it('should deletes an entity', async () => {
    const entity = new StubEntity({ name: 'name value', price: 5 });
    await repository.create(entity);

    await repository.delete(entity.id);
    expect(repository.data).toHaveLength(0);

    await repository.create(entity);

    await repository.delete(entity.uniqueEntityId);
    expect(repository.data).toHaveLength(0);
  });
});
