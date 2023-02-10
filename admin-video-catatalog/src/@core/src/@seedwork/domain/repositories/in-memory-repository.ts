import { Entity } from '../entities';
import { NotFoundError } from '../errors';
import { UniqueEntityId } from '../value-objects';
import {
  RepositoryInterface,
  SearchableRepositoryInterface,
  SearchParams,
  SearchResult,
  SortDirection,
} from './respository';

export abstract class InMemoryRepository<T extends Entity>
  implements RepositoryInterface<T>
{
  public data: T[] = [];

  async create(entity: T): Promise<void> {
    this.data.push(entity);
  }

  async findById(id: string | UniqueEntityId): Promise<T> {
    return this._get(id);
  }

  async findAll(): Promise<T[]> {
    return this.data;
  }

  async update(entity: T): Promise<void> {
    await this._get(entity.id);
    const indexFound = this.data.findIndex((item) => item.id === entity.id);
    this.data[indexFound] = entity;
  }

  async delete(id: string | UniqueEntityId): Promise<void> {
    await this._get(`${id}`);
    const indexFound = this.data.findIndex((item) => item.id === `${id}`);
    this.data.splice(indexFound, 1);
  }

  protected async _get(id: string | UniqueEntityId): Promise<T> {
    const item = this.data.find((item) => item.id === `${id}`);
    if (!item) throw new NotFoundError(`Not found using ID ${id}`);
    return item;
  }
}

export abstract class InMemorySearchableRepository<T extends Entity>
  extends InMemoryRepository<T>
  implements SearchableRepositoryInterface<T, any, any>
{
  sortableFields: string[] = [];

  async search(params: SearchParams): Promise<SearchResult<T>> {
    const dataFiltered = await this.applyFilter(this.data, params.filter);
    const dataSorted = await this.applySort(
      dataFiltered,
      params.sort,
      params.sort_dir,
    );
    const dataPaginated = await this.applyPaginate(
      dataSorted,
      params.page,
      params.per_page,
    );

    return new SearchResult({
      data: dataPaginated,
      total: dataFiltered.length,
      current_page: params.page,
      sort: params.sort,
      sort_dir: params.sort_dir,
      filter: params.filter,
      per_page: params.per_page,
    });
  }

  protected abstract applyFilter(
    data: T[],
    filter: SearchParams['filter'],
  ): Promise<T[]>;

  protected async applySort(
    data: T[],
    sort: SearchParams['sort'],
    sort_dir: SortDirection | null,
  ): Promise<T[]> {
    if (!sort || !this.sortableFields.includes(sort)) {
      return data;
    }

    return [...data].sort((a, b) => {
      if (a.props[sort] < b.props[sort]) {
        return sort_dir === 'asc' ? -1 : 1;
      }

      if (a.props[sort] > b.props[sort]) {
        return sort_dir === 'asc' ? 1 : -1;
      }

      return 0;
    });
  }

  protected async applyPaginate(
    data: T[],
    page: SearchParams['page'],
    per_page: SearchParams['per_page'],
  ): Promise<T[]> {
    const start = (page - 1) * per_page;
    const limit = start + per_page;
    return data.slice(start, limit);
  }
}
