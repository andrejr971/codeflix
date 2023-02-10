import { CreateCategoryUseCase } from '@core/src/category/application';
import { CategoryInMemoryRepository } from '@core/src/category/infra';

describe('Create category usecase unit test', () => {
  let useCase: CreateCategoryUseCase;
  let repository: CategoryInMemoryRepository;

  beforeEach(() => {
    repository = new CategoryInMemoryRepository();

    useCase = new CreateCategoryUseCase(repository);
  });

  it('should be able create a category', async () => {
    const repositorySpy = jest.spyOn(repository, 'create');
    let category = await useCase.execute({
      name: 'test',
    });

    expect(repositorySpy).toBeCalledTimes(1);

    expect(category).toHaveProperty('id');
    expect(category.name).toBe('test');
    expect(category).toStrictEqual(repository.data[0].toJson());

    category = await useCase.execute({
      name: 'test',
      description: 'desc',
      is_active: false,
    });

    expect(category).toHaveProperty('id');
    expect(category.is_active).toBeFalsy();
  });
});
