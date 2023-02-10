import { Category } from '@core/src/category/domain';

export namespace CategoryDTO {
  export type Params = {
    name: string;
    description?: string;
    is_active?: boolean;
  };

  export type Response = {
    id: string;
    name: string;
    description: string | null;
    is_active: boolean;
    created_at: Date;
  };
}

export class CategoryResponseMapper {
  static toResponse(category: Category): CategoryDTO.Response {
    return category.toJson();
  }
}
