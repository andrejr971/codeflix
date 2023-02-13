import { SearchResult } from '../../domain';

export type PaginationResponseDTO<Data = any> = {
  data: Data[];
  total: number;
  current_page: number;
  last_page: number;
  per_page: number;
};

export class PaginationResponseMapper {
  static toResponse<Data = any>(data: Data[], result: SearchResult) {
    return {
      data,
      total: result.total,
      current_page: result.current_page,
      last_page: result.last_page,
      per_page: result.per_page,
    };
  }
}
