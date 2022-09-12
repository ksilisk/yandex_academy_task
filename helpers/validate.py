"""
Тут проводится вся валидация данных, полученных от пользователя
"""
import db.sqllib as sql
import datetime
import logging


# общая валидация входных данных при добавлении новых файлов
# data - данные post-запроса
def valid_data(data):
    logging.info('Validating data!')
    if not data.get('items'):
        return False
    if not valid_date(data.get('updateDate')):
        return False
    temp = {}
    parents = []
    for i in range(len(data['items'])):
        if not valid_item(data['items'][i], parents):
            return False
        if temp.get(data['items'][i]['id']):
            return False
        temp[data['items'][i]['id']] = 1
    return True


# функция, определяющая валиден ли конкретный файл
# data - отдельно взятый item из import'а
def valid_item(data, parents):
    if not type(data['id']) == str or len(data['id']) <= 0:
        return False
    if not data['type'] in ['FILE', 'FOLDER']:
        return False
    if data['parentId']:
        if not type(data['parentId']) == str:
            return False
        if sql.get_type(data['parentId']) == 0:
            return False
        if not data['parentId'] in parents:
            if not sql.check_id(data['parentId']):
                return False
    if data['type'] == 'FOLDER':
        if sql.check_id(data['id']):
            if 1 != sql.get_type(data['id']):
                return False
        if data['id'] == data['parentId']:
            return False
        parents.append(data['id'])
    else:
        if sql.check_id(data['id']):
            if 0 != sql.get_type(data['id']):
                return False
        if not (type(data.get('url')) == str) or len(data['url']) > 255:
            return False
        if not (type(data.get('size')) == int) or data['size'] <= 0:
            return False
        if sql.get_id(data['url']) and data['id'] != sql.get_id(data['url']):
            return False
    return True


# функция, определяющая валидна ли дата
# date - дата в формате string
def valid_date(date):
    logging.info('Validating date!')
    try:
        datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%fZ')
        return True
    except:
        return False


# функция, определяющая наличие id в базе и его валидность
# elem_id - id проверяемого элемента
def valid_id(elem_id):
    logging.info('Validating id!')
    if not type(elem_id) == str or len(elem_id) <= 0 or not sql.check_id(elem_id):
        return False
    return True
