import { NotFoundError } from '@core/src/@seedwork/domain';
import { GetCategoryByIdUseCase } from '@core/src/category/application';
import { Category } from '@core/src/category/domain';
import { CategoryInMemoryRepository } from '@core/src/category/infra';

describe('Create category usecase unit test', () => {
  let useCase: GetCategoryByIdUseCase;
  let repository: CategoryInMemoryRepository;

  beforeEach(() => {
    repository = new CategoryInMemoryRepository();

    useCase = new GetCategoryByIdUseCase(repository);
  });

  it('should throws error when entity not found', async () => {
    expect(() => useCase.execute({ id: 'fake id' })).rejects.toThrow(
      new NotFoundError('Not found using ID fake id'),
    );
  });

  it('should returns a category', async () => {
    const data = [new Category({ name: 'Movie' })];
    repository.data = data;
    const spyFindById = jest.spyOn(repository, 'findById');
    const category = await useCase.execute({ id: data[0].id });
    expect(spyFindById).toHaveBeenCalledTimes(1);
    expect(category).toStrictEqual({
      id: data[0].id,
      name: 'Movie',
      description: null,
      is_active: true,
      created_at: data[0].created_at,
    });
  });
});
