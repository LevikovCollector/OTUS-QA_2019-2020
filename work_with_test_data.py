from contextlib import contextmanager
import csv
import json


@contextmanager
def read_csv_file(path):
    try:
        csv_file = open(path, 'r')
        yield csv_file
    except OSError:
        print('Возникла ошибка при работе с файлом')
    finally:
        csv_file.close()


@contextmanager
def read_json_file(path):
    try:
        json_file = open(path, 'r')
        yield json_file

    except OSError:
        print('Возникла ошибка при работе с файлом')
    finally:
        json_file.close()


@contextmanager
def create_result_json(path):
    try:
        new_json = open(path, 'w')
        yield new_json
    except OSError:
        print('Возникла ошибка при работе с файлом')
    finally:
        new_json.close()


def create_list_for_json(books_inf, users_inf):
    user_with_books = []
    for index in range(0, len(users_inf)):
        user_with_books.append({'name': users_inf[index][0],
                                'gender': users_inf[index][1],
                                'address': users_inf[index][2],
                                'books': [{'title': books_inf[index][0],
                                           'author': books_inf[index][1],
                                           'height': books_inf[index][2]
                                           }]
                                })
    return user_with_books


if __name__ == '__main__':
    books_information = []
    with read_csv_file('./data/books.csv') as file_csv:
        csv_reader = csv.reader(file_csv)
        for row in csv_reader:
            books_information.append((row[0], row[1], row[3]))
        del books_information[0]

    json_information = []
    with read_json_file('./data/users.json') as file_json:
        data = json.load(file_json)
        for row in data:
            json_information.append((row['name'], row['gender'], row['address']))

    with create_result_json('./data/result.json') as new_json:
        new_json.write(json.dumps(create_list_for_json(books_information, json_information)))
