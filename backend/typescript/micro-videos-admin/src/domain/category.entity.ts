export type CategoryConstructorProps = {
  category_id?: string;
  name: string;
  description?: string | null;
  is_active?: boolean;
  created_at?: Date;
};

export class Category {
  category_id?: string;
  name: string;
  description: string | null;
  is_active: boolean;
  created_at: Date;

  constructor({
    category_id,
    name,
    description,
    is_active,
    created_at,
  }: CategoryConstructorProps) {
    this.category_id = category_id;
    this.name = name;
    this.description = description ?? null;
    this.is_active = is_active ?? true;
    this.created_at = created_at ?? new Date();
  }

  static create(props: CategoryConstructorProps) {
    return new Category(props);
  }

  changeName(name: string) {
    this.name = name;
  }

  changeDescription(description: string) {
    this.description = description;
  }

  activate() {
    this.is_active = true;
  }

  deactivate() {
    this.is_active = false;
  }

  toJSON() {
    return {
      category_id: this.category_id,
      name: this.name,
      description: this.description,
      is_active: this.is_active,
      created_at: this.created_at,
    };
  }
}
