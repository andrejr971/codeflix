import { omit } from 'lodash';

import { UniqueEntityId } from '@core/src/@seedwork/domain';
import { Category, CategoryProps } from '@core/src/category/domain';

describe('Category unit test', () => {
  beforeEach(() => {
    Category.validate = jest.fn();
  });

  test('construct of category ', () => {
    let created_at = new Date();

    let category: Category = new Category({
      name: 'Movie',
    });
    let props = omit(category.props, 'created_at');
    expect(props).toStrictEqual({
      name: 'Movie',
      description: null,
      is_active: true,
    });
    expect(category.created_at).toBeInstanceOf(Date);

    category = new Category({
      name: 'Movie',
      description: 'some description',
      is_active: false,
      created_at,
    });
    expect(category.props).toStrictEqual({
      name: 'Movie',
      description: 'some description',
      is_active: false,
      created_at,
    });

    category = new Category({
      name: 'Movie',
      description: 'other description',
    });
    expect(category.props).toMatchObject({
      name: 'Movie',
      description: 'other description',
    });

    category = new Category({
      name: 'Movie',
      is_active: true,
    });
    expect(category.props).toMatchObject({
      name: 'Movie',
      is_active: true,
    });

    category = new Category({
      name: 'Movie',
    });
    expect(category.is_active).toBeTruthy();

    category = new Category({
      name: 'Movie',
      created_at,
    });
    expect(category.props).toMatchObject({
      name: 'Movie',
      created_at,
    });
  });

  test('id shield', () => {
    type CategoryData = {
      props: CategoryProps;
      id?: UniqueEntityId;
    };

    const data: CategoryData[] = [
      {
        props: {
          name: 'movie',
        },
      },
      {
        props: {
          name: 'movie',
        },
        id: null,
      },
      {
        props: {
          name: 'movie',
        },
        id: undefined,
      },
      {
        props: {
          name: 'movie',
        },
        id: new UniqueEntityId(),
      },
    ];

    data.forEach((index) => {
      let category = new Category(index.props, index.id);
      expect(category.id).not.toBeNull();
      expect(category.uniqueEntityId).toBeInstanceOf(UniqueEntityId);
    });
  });

  test('getter of name props', () => {
    const category = new Category({
      name: 'movie',
    });
    expect(category.name).toBe('movie');
  });

  test('getter and setter of description props', () => {
    let category = new Category({
      name: 'movie',
    });
    expect(category.name).toBe('movie');
    expect(category.description).toBeNull();

    category = new Category({
      name: 'movie',
      description: 'some description',
    });
    expect(category.description).toBe('some description');

    category = new Category({
      name: 'movie',
    });
    category['description'] = 'other description';
    expect(category.description).toBe('other description');

    category['description'] = undefined;
    expect(category.description).toBeNull();
  });

  test('getter and setter of is_active props', () => {
    let category = new Category({
      name: 'movie',
    });
    expect(category.name).toBe('movie');
    expect(category.is_active).toBeTruthy();

    category = new Category({
      name: 'movie',
      is_active: false,
    });
    expect(category.is_active).toBeFalsy();

    category = new Category({
      name: 'movie',
    });
    category['is_active'] = false;
    expect(category.is_active).toBeFalsy();

    category = new Category({
      name: 'movie',
    });
    category['is_active'] = undefined;
    expect(category.is_active).toBeTruthy();
  });

  test('getter of created_at props', () => {
    let category = new Category({
      name: 'movie',
    });
    expect(category.created_at).toBeInstanceOf(Date);

    const created_at = new Date();

    category = new Category({
      name: 'movie',
      created_at,
    });
    expect(category.created_at).toBe(created_at);
  });

  it('should update a category', () => {
    const category = new Category({ name: 'Movie' });
    category.update('Documentary', 'some description');
    expect(Category.validate).toHaveBeenCalledTimes(2);
    expect(category.name).toBe('Documentary');
    expect(category.description).toBe('some description');
  });

  it('should active a category', () => {
    const category = new Category({
      name: 'Filmes',
      is_active: false,
    });
    category.activate();
    expect(category.is_active).toBeTruthy();
  });

  test('should disable a category', () => {
    const category = new Category({
      name: 'Filmes',
      is_active: true,
    });
    category.deactivate();
    expect(category.is_active).toBeFalsy();
  });
});
