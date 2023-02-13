import { UseCase } from '@core/src/@seedwork/application';
import { CategoryRepository } from '@core/src/category/domain';
import { CategoryDTO, CategoryResponseMapper } from '../../dtos';
import { UpdateCategoryUseCaseDTO } from './update-category-usecase-dto';

export class UpdateCategoryUseCase
  implements
    UseCase<UpdateCategoryUseCaseDTO.Params, UpdateCategoryUseCaseDTO.Response>
{
  constructor(private categoryRepository: CategoryRepository.Repository) {}

  async execute(
    data: UpdateCategoryUseCaseDTO.Params,
  ): Promise<CategoryDTO.Response> {
    const category = await this.categoryRepository.findById(data.id);
    category.update(data.name, data.description);

    if (data.is_active === true) {
      category.activate();
    }

    if (data.is_active === false) {
      category.deactivate();
    }

    await this.categoryRepository.update(category);

    return CategoryResponseMapper.toResponse(category);
  }
}
