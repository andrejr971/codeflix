import { NotFoundError } from '@core/src/@seedwork/domain';
import { DeleteCategoryUseCase } from '@core/src/category/application';
import { Category } from '@core/src/category/domain';
import { CategoryInMemoryRepository } from '@core/src/category/infra';

describe('DeleteCategoryUseCase Unit Tests', () => {
  let useCase: DeleteCategoryUseCase;
  let repository: CategoryInMemoryRepository;

  beforeEach(() => {
    repository = new CategoryInMemoryRepository();
    useCase = new DeleteCategoryUseCase(repository);
  });

  it('should throws error when entity not found', async () => {
    await expect(() => useCase.execute({ id: 'fake id' })).rejects.toThrow(
      new NotFoundError(`Not found using ID fake id`),
    );
  });

  it('should delete a category', async () => {
    const data = [new Category({ name: 'test 1' })];
    repository.data = data;
    await useCase.execute({
      id: data[0].id,
    });
    expect(repository.data).toHaveLength(0);
  });
});
