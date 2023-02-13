import {
  PaginationResponseMapper,
  UseCase,
} from '@core/src/@seedwork/application';
import { CategoryRepository } from '@core/src/category/domain';
import { CategoryResponseMapper } from '../../dtos';
import { GetListCategoriesUseCaseDTO } from './get-list-categories-usecase-dto';

export class GetListCategoriesUseCase
  implements
    UseCase<
      GetListCategoriesUseCaseDTO.Params,
      GetListCategoriesUseCaseDTO.Response
    >
{
  constructor(private categoryRepository: CategoryRepository.Repository) {}

  async execute(
    data: GetListCategoriesUseCaseDTO.Params,
  ): Promise<GetListCategoriesUseCaseDTO.Response> {
    const params = new CategoryRepository.Params(data);
    const searchResult = await this.categoryRepository.search(params);
    return this.toResponse(searchResult);
  }

  private toResponse(
    searchResult: CategoryRepository.Response,
  ): GetListCategoriesUseCaseDTO.Response {
    const items = searchResult.data.map((item) => {
      return CategoryResponseMapper.toResponse(item);
    });
    return PaginationResponseMapper.toResponse(items, searchResult);
  }
}
