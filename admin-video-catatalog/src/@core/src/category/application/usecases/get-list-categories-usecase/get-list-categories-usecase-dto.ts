import {
  PaginationResponseDTO,
  SearchParamsDTO,
} from '@core/src/@seedwork/application';
import { CategoryDTO } from '../../dtos';

export namespace GetListCategoriesUseCaseDTO {
  export type Params = SearchParamsDTO;

  export type Response = PaginationResponseDTO<CategoryDTO.Response>;
}
