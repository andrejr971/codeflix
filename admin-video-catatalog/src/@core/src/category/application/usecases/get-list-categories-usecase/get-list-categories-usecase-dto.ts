import { PaginationResponseDTO, SearchParamsDTO } from '#seedwork/application';
import { CategoryDTO } from '../../dtos';

export namespace GetListCategoriesUseCaseDTO {
  export type Params = SearchParamsDTO;

  export type Response = PaginationResponseDTO<CategoryDTO.Response>;
}
