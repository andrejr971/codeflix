import {Uuid} from '@/shared/domain/value-objects/uuid.vo';

import {Category} from '../category.entity';

describe('Category unit tests', () => {
  let validateSpy: any;
  beforeEach(() => {
    validateSpy = jest.spyOn(Category, 'validate');
  });

  describe('constructor', () => {
    test('should create a category with default values', () => {
      const category = new Category({
        name: 'Movie',
      });
      expect(category.category_id).toBeInstanceOf(Uuid);
      expect(category.name).toBe('Movie');
      expect(category.description).toBeNull();
      expect(category.is_active).toBeTruthy();
      expect(category.created_at).toBeInstanceOf(Date);
    });

    test('should create a new Category with all values', () => {
      const category = new Category({
        name: 'Movie',
        description: 'some description',
      });

      expect(category).toBeInstanceOf(Category);
      expect(category.category_id).toBeInstanceOf(Uuid);
      expect(category.name).toBe('Movie');
      expect(category.description).toBe('some description');
      expect(category.is_active).toBe(true);
      expect(category.created_at).toBeInstanceOf(Date);
    });
  });

  describe('category_id field', () => {
    const arrange = [
      {category_id: null},
      {category_id: undefined},
      {category_id: new Uuid()},
    ];
    test.each(arrange)('id = %j', ({category_id}) => {
      const category = new Category({
        name: 'Movie',
        category_id: category_id as any,
      });
      expect(category.category_id).toBeInstanceOf(Uuid);
      if (category_id instanceof Uuid) {
        expect(category.category_id).toBe(category_id);
      }
    });
  });

  describe('method create', () => {
    test('should create a new Category', () => {
      const category = Category.create({
        name: 'Category 1',
        description: 'Category 1 description',
      });

      expect(category).toBeInstanceOf(Category);
      expect(category.category_id).toBeInstanceOf(Uuid);
      expect(category.name).toBe('Category 1');
      expect(category.description).toBe('Category 1 description');
      expect(category.is_active).toBe(true);
      expect(category.created_at).toBeInstanceOf(Date);
      expect(validateSpy).toHaveBeenCalledTimes(1);
    });

    test('should create a category with description', () => {
      const category = Category.create({
        name: 'Category 1',
        description: 'Category 1 description',
      });

      expect(category.category_id).toBeInstanceOf(Uuid);
      expect(category.name).toBe('Category 1');
      expect(category.description).toBe('Category 1 description');
      expect(category.is_active).toBe(true);
      expect(category.created_at).toBeInstanceOf(Date);
      expect(validateSpy).toHaveBeenCalledTimes(1);
    });

    test('should create a category with is_active false', () => {
      const category = Category.create({
        name: 'Category 1',
        is_active: false,
      });
      expect(category.category_id).toBeInstanceOf(Uuid);
      expect(category.name).toBe('Category 1');
      expect(category.description).toBeNull();
      expect(category.is_active).toBe(false);
      expect(category.created_at).toBeInstanceOf(Date);
      expect(validateSpy).toHaveBeenCalledTimes(1);
    });
  });

  test('should change the name of the category', () => {
    const category = new Category({
      name: 'Category 1',
    });

    category.changeName('Category 2');
    expect(category.name).toBe('Category 2');
    expect(validateSpy).toHaveBeenCalledTimes(1);
  });

  test('should change the description of the category', () => {
    const category = new Category({
      name: 'Category 1',
    });

    category.changeDescription('Category 1 description');
    expect(category.description).toBe('Category 1 description');
    expect(validateSpy).toHaveBeenCalledTimes(1);
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
