import { UseCase } from '@core/src/@seedwork/application';
import { CategoryRepository } from '@core/src/category/domain';
import { CategoryResponseMapper } from '@core/src/category/application';
import { GetCategoryByIdUseCaseNamespace } from './get-category-by-id-usecase-dto';

export class GetCategoryByIdUseCase
  implements
    UseCase<
      GetCategoryByIdUseCaseNamespace.Params,
      GetCategoryByIdUseCaseNamespace.Response
    >
{
  constructor(private categoryRepository: CategoryRepository.Repository) {}

  async execute({
    id,
  }: GetCategoryByIdUseCaseNamespace.Params): Promise<GetCategoryByIdUseCaseNamespace.Response> {
    const category = await this.categoryRepository.findById(id);
    return CategoryResponseMapper.toResponse(category);
  }
}
