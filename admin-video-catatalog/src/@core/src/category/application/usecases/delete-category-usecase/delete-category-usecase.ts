import { UseCase } from '#seedwork/application';
import { CategoryRepository } from '#category/domain';
import { DeleteCategoryUseCaseDTO } from './delete-category-usecase-dto';

export class DeleteCategoryUseCase
  implements
    UseCase<DeleteCategoryUseCaseDTO.Params, DeleteCategoryUseCaseDTO.Response>
{
  constructor(private categoryRepository: CategoryRepository.Repository) {}

  async execute({ id }: DeleteCategoryUseCaseDTO.Params): Promise<void> {
    await this.categoryRepository.delete(id);
  }
}
