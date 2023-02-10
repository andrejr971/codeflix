import { UseCase } from '@core/src/@seedwork/application';
import { Category, CategoryRepository } from '@core/src/category/domain';
import { CategoryResponseMapper } from '@core/src/category/application';
import { CreateCategoryUseCaseNamespace } from './create-category-usecase-dto';

export class CreateCategoryUseCase
  implements
    UseCase<
      CreateCategoryUseCaseNamespace.Params,
      CreateCategoryUseCaseNamespace.Response
    >
{
  constructor(private categoryRepository: CategoryRepository.Repository) {}

  async execute(
    data: CreateCategoryUseCaseNamespace.Params,
  ): Promise<CreateCategoryUseCaseNamespace.Response> {
    const category = new Category(data);
    await this.categoryRepository.create(category);
    return CategoryResponseMapper.toResponse(category);
  }
}
