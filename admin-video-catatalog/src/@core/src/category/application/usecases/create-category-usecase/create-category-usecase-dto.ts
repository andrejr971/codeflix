import { CategoryDTO } from '@core/src/category/application';

export namespace CreateCategoryUseCaseDTO {
  export type Params = CategoryDTO.Params;

  export type Response = CategoryDTO.Response;
}
