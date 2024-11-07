import {Op} from 'sequelize';

import {Category} from '@core/category/domain/category.entity';
import {
  CategorySearchParams,
  CategorySearchResult,
} from '@core/category/domain/category.repository';
import {NotFoundError} from '@core/shared/domain/errors/not-found.error';
import type {ISearchableRepository} from '@core/shared/domain/repository/repository.interface';
import {Uuid} from '@core/shared/domain/value-objects/uuid.vo';

import {CategoryModel} from './category.model';
import {CategoryModelMapper} from './category-model-mapper';

export class CategorySequelizeRepository
  implements ISearchableRepository<Category, Uuid>
{
  sortableFields: string[] = ['name', 'created_at'];

  constructor(private categoryModel: typeof CategoryModel) {}

  async insert(entity: Category): Promise<void> {
    const modelProps = CategoryModelMapper.toModel(entity);
    await this.categoryModel.create(modelProps.toJSON());
  }

  async bulkInsert(entities: Category[]): Promise<void> {
    const modelsProps = entities.map((entity) =>
      CategoryModelMapper.toModel(entity).toJSON(),
    );
    await this.categoryModel.bulkCreate(modelsProps);
  }

  async findById(category_id: Uuid): Promise<Category | null> {
    const model = await this._get(category_id.id);
    return model ? CategoryModelMapper.toEntity(model) : null;
  }

  async findAll(): Promise<Category[]> {
    const models = await this.categoryModel.findAll();
    return models.map((model) => CategoryModelMapper.toEntity(model));
  }

  private async _get(category_id: string) {
    return this.categoryModel.findByPk(category_id);
  }

  async update(entity: Category): Promise<void> {
    const id = entity.category_id.id;

    const model = await this._get(id);
    if (!model) {
      throw new NotFoundError(id, this.getEntity());
    }
    const modelProps = CategoryModelMapper.toModel(entity);

    await this.categoryModel.update(modelProps.toJSON(), {
      where: {
        category_id: id,
      },
    });
  }

  async delete(category_id: Uuid): Promise<void> {
    const id = category_id.id;

    const model = await this._get(id);
    if (!model) {
      throw new NotFoundError(id, this.getEntity());
    }

    await this.categoryModel.destroy({
      where: {category_id: id},
    });
  }

  async search(props: CategorySearchParams): Promise<CategorySearchResult> {
    const offset = (props.page - 1) * props.per_page;
    const limit = props.per_page;

    const {count, rows: models} = await this.categoryModel.findAndCountAll({
      ...(props.filter && {
        where: {
          name: {[Op.like]: `%${props.filter}%`},
        },
      }),
      ...(props.sort && this.sortableFields.includes(props.sort)
        ? {order: [[props.sort, props.sort_dir]]}
        : // {order: this.formatSort(props.sort, props.sort_dir!)}
          {order: [['created_at', 'desc']]}),
      offset,
      limit,
    });

    return new CategorySearchResult({
      items: models.map((model) => CategoryModelMapper.toEntity(model)),
      current_page: props.page,
      per_page: props.per_page,
      total: count,
    });
  }

  getEntity(): new (...args: any[]) => Category {
    return Category;
  }
}
