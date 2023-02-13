import { UseCase } from '#seedwork/application';
import { CategoryRepository } from '#category/domain';
import { CategoryResponseMapper } from '#category/application';
import { GetCategoryByIdUseCaseDTO } from './get-category-by-id-usecase-dto';

export class GetCategoryByIdUseCase
  implements
    UseCase<
      GetCategoryByIdUseCaseDTO.Params,
      GetCategoryByIdUseCaseDTO.Response
    >
{
  constructor(private categoryRepository: CategoryRepository.Repository) {}

  async execute({
    id,
  }: GetCategoryByIdUseCaseDTO.Params): Promise<GetCategoryByIdUseCaseDTO.Response> {
    const category = await this.categoryRepository.findById(id);
    return CategoryResponseMapper.toResponse(category);
  }
}
