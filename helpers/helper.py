'''
Тут хранятся все функции для обработки различных запросов к API
'''

import db.sqllib as sql
import logging


# функция, которая добавляет данные в базу
# data - данные, полученные от пользователя
def import_help(data):
    logging.info('import_help func')
    for i in range(len(data['items'])):
        sql.add_item(data['items'][i], data['updateDate'])
        temp = data['items'][i]['parentId']
        while temp:
            sql.update_date(temp, data['updateDate'])
            temp = sql.get_parent(temp)


# функция, удаляющая элемент
# если папка, то удаляет ее и все содержимое в ней
# elem_id - id элемента
def delete_help(elem_id, date):
    logging.info('delete_help func')
    temp = sql.get_parent(elem_id)
    while temp:
        sql.update_date(temp, date)
        temp = sql.get_parent(temp)
    if sql.get_type(elem_id):
        files = sql.get_folder_files(elem_id)
        for i in range(len(files)):
            delete_help(files[i][0], date)
        sql.del_item(elem_id)
    else:
        sql.del_item(elem_id)


# функция, возвращающая файлы, которые были обновлены в заданный период
# date - дата, полученная от пользователя
def updates_help(date):
    logging.info('updates_help func')
    updated_files = sql.get_files_updated(date)
    result = {
        'items': []
    }
    for file in updated_files:
        result['items'].append({
            'id': file[0],
            'url': file[1],
            'date': file[2],
            'parentId': file[3],
            'size': file[5],
            'type': 'FILE'
        })
    return result


# функция, собирающая данные об элементе
# elem_id - id элемента
def nodes_help(elem_id):
    logging.info('nodes_help func')
    data = sql.get_item(elem_id)
    result = {'id': data[0], 'url': data[1], 'date': data[2], 'parentId': data[3],
              'type': 'FOLDER' if data[4] else 'FILE', 'size': data[5]}
    if result['type'] == 'FOLDER':
        result['children'] = []
        files = sql.get_folder_files(elem_id)
        for i in range(len(files)):
            result['children'].append(nodes_help(files[i][0]))
        result['size'] = sum_size(result['children'])
    else:
        result['children'] = None
    return result


# функция, подсчитывающая размер папки
# children - список файлов внутри папки
def sum_size(children):
    result = 0
    for i in range(len(children)):
        result += children[i]['size']
    return result
