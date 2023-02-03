import {
  Entity,
  UniqueEntityId,
  EntityValidationError,
} from '@core/src/@seedwork/domain';
import { CategoryValidatorFactory } from '../../main/factories/category-factory';

export type CategoryProps = {
  name: string;
  is_active?: boolean;
  description?: string;
  created_at?: Date;
};

export class Category extends Entity<CategoryProps> {
  constructor(public readonly props: CategoryProps, id?: UniqueEntityId) {
    super(props, id);
    Category.validate(props);
    this.description = this.props.description;
    this.is_active = this.props.is_active ?? true;
    this.props.created_at = this.props.created_at ?? new Date();
  }

  update(name: string, description: string): void {
    Category.validate({
      name,
      description,
    });
    this.name = name;
    this.description = description;
  }

  static validate(props: CategoryProps) {
    const validator = CategoryValidatorFactory.create();
    const isValid = validator.validate(props);
    if (!isValid) {
      throw new EntityValidationError(validator.errors);
    }
  }

  activate() {
    this.props.is_active = true;
  }

  deactivate() {
    this.props.is_active = false;
  }

  get name(): string {
    return this.props.name;
  }

  private set name(name: string) {
    this.props.name = name;
  }

  get description(): string {
    return this.props.description;
  }

  private set description(description: string) {
    this.props.description = description ?? null;
  }

  get is_active(): boolean {
    return this.props.is_active;
  }

  private set is_active(is_active: boolean) {
    this.props.is_active = is_active ?? true;
  }

  get created_at(): Date {
    return this.props.created_at;
  }
}
