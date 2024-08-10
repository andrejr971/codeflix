import {Category} from '../category.entity';

describe('Category unit tests', () => {
  describe('constructor', () => {
    test('should create a category with default values', () => {
      const category = new Category({
        name: 'Movie',
      });
      expect(category.category_id).toBeUndefined();
      expect(category.name).toBe('Movie');
      expect(category.description).toBeNull();
      expect(category.is_active).toBeTruthy();
      expect(category.created_at).toBeInstanceOf(Date);
    });

    test('should create a new Category with all values', () => {
      const category = new Category({
        name: 'Category 1',
        description: 'Category 1 description',
      });

      expect(category).toBeInstanceOf(Category);
      expect(category).toEqual({
        category_id: undefined,
        name: 'Category 1',
        description: 'Category 1 description',
        is_active: true,
        created_at: expect.any(Date),
      });
    });
  });

  describe('method create', () => {
    test('should create a new Category', () => {
      const category = Category.create({
        name: 'Category 1',
        description: 'Category 1 description',
      });

      expect(category).toBeInstanceOf(Category);
      expect(category).toEqual({
        category_id: undefined,
        name: 'Category 1',
        description: 'Category 1 description',
        is_active: true,
        created_at: expect.any(Date),
      });
    });

    test('should create a category with description', () => {
      const category = Category.create({
        name: 'Category 1',
        description: 'Category 1 description',
      });

      expect(category).toEqual({
        category_id: undefined,
        name: 'Category 1',
        description: 'Category 1 description',
        is_active: true,
        created_at: expect.any(Date),
      });
    });

    test('should create a category with is_active false', () => {
      const category = Category.create({
        name: 'Category 1',
        is_active: false,
      });

      expect(category).toEqual({
        category_id: undefined,
        name: 'Category 1',
        description: null,
        is_active: false,
        created_at: expect.any(Date),
      });
    });
  });

  test('should change the name of the category', () => {
    const category = new Category({
      name: 'Category 1',
    });

    category.changeName('Category 2');
    expect(category.name).toBe('Category 2');
  });

  test('should change the description of the category', () => {
    const category = new Category({
      name: 'Category 1',
    });

    category.changeDescription('Category 1 description');
    expect(category.description).toBe('Category 1 description');
  });

  test('should activate the category', () => {
    const category = new Category({
      name: 'Category 1',
    });

    category.deactivate();
    expect(category.is_active).toBeFalsy();
  });

  test('should deactivate the category', () => {
    const category = new Category({
      name: 'Category 1',
    });

    category.activate();
    expect(category.is_active).toBeTruthy();
  });
});
