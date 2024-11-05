import {Category} from '@/category/domain/category.entity';
import type {ICategoryRepository} from '@/category/domain/category.repository';
import type {IUseCase} from '@/shared/application/use-case.interface';

import {CategoryOutput, CategoryOutputMapper} from './common/category-output';

export type CreateCategoryInput = {
  name: string;
  description?: string | null;
  is_active?: boolean;
};

export type CreateCategoryOutput = CategoryOutput;

export class CreateCategoryUseCase
  implements IUseCase<CreateCategoryInput, CreateCategoryOutput>
{
  constructor(private repository: ICategoryRepository) {}

  async execute(params: CreateCategoryInput): Promise<CreateCategoryOutput> {
    const category = Category.create(params);
    await this.repository.insert(category);

    return CategoryOutputMapper.toOutput(category);
  }
}
