import { GetListCategoriesUseCase } from '#category/application';
import { Category, CategoryRepository } from '#category/domain';
import { CategoryInMemoryRepository } from '#category/infra';

describe('GetListCategoriesUseCase Unit Tests', () => {
  let useCase: GetListCategoriesUseCase;
  let repository: CategoryInMemoryRepository;

  beforeEach(() => {
    repository = new CategoryInMemoryRepository();
    useCase = new GetListCategoriesUseCase(repository);
  });

  test('toResponse method', () => {
    let result = new CategoryRepository.Response({
      data: [],
      total: 1,
      current_page: 1,
      per_page: 2,
      sort: null,
      sort_dir: null,
      filter: null,
    });
    let output = useCase['toResponse'](result);
    expect(output).toStrictEqual({
      data: [],
      total: 1,
      current_page: 1,
      per_page: 2,
      last_page: 1,
    });

    const entity = new Category({ name: 'Movie' });
    result = new CategoryRepository.Response({
      data: [entity],
      total: 1,
      current_page: 1,
      per_page: 2,
      sort: null,
      sort_dir: null,
      filter: null,
    });

    output = useCase['toResponse'](result);
    expect(output).toStrictEqual({
      data: [entity.toJson()],
      total: 1,
      current_page: 1,
      per_page: 2,
      last_page: 1,
    });
  });

  it('should returns output using empty input with categories ordered by created_at', async () => {
    const items = [
      new Category({ name: 'test 1' }),
      new Category({
        name: 'test 2',
        created_at: new Date(new Date().getTime() + 100),
      }),
    ];
    repository.data = items;

    const output = await useCase.execute({});
    expect(output).toStrictEqual({
      data: [...items].reverse().map((i) => i.toJson()),
      total: 2,
      current_page: 1,
      per_page: 15,
      last_page: 1,
    });
  });

  it('should returns output using pagination, sort and filter', async () => {
    const items = [
      new Category({ name: 'a' }),
      new Category({
        name: 'AAA',
      }),
      new Category({
        name: 'AaA',
      }),
      new Category({
        name: 'b',
      }),
      new Category({
        name: 'c',
      }),
    ];
    repository.data = items;

    let output = await useCase.execute({
      page: 1,
      per_page: 2,
      sort: 'name',
      filter: 'a',
    });
    expect(output).toStrictEqual({
      data: [items[1].toJson(), items[2].toJson()],
      total: 3,
      current_page: 1,
      per_page: 2,
      last_page: 2,
    });

    output = await useCase.execute({
      page: 2,
      per_page: 2,
      sort: 'name',
      filter: 'a',
    });
    expect(output).toStrictEqual({
      data: [items[0].toJson()],
      total: 3,
      current_page: 2,
      per_page: 2,
      last_page: 2,
    });

    output = await useCase.execute({
      page: 1,
      per_page: 2,
      sort: 'name',
      sort_dir: 'desc',
      filter: 'a',
    });
    expect(output).toStrictEqual({
      data: [items[0].toJson(), items[2].toJson()],
      total: 3,
      current_page: 1,
      per_page: 2,
      last_page: 2,
    });
  });
});
