import { CategoryDTO } from '../../dtos';

export namespace UpdateCategoryUseCaseDTO {
  export type Params = CategoryDTO.Params & {
    id: string;
  };

  export type Response = CategoryDTO.Response;
}
