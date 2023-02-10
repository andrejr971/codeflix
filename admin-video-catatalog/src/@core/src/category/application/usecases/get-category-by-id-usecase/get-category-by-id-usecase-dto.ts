import { CategoryDTO } from '../../dtos';

export namespace GetCategoryByIdUseCaseNamespace {
  export type Params = {
    id: string;
  };

  export type Response = CategoryDTO.Response;
}
