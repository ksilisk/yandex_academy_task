"""
Тут лежат все необходимые обращения к базе данных
"""

import sqlite3
import logging

con = sqlite3.connect('db/database.db', check_same_thread=False)
cur = con.cursor()


# получение типа элемента
# возвращаемые данные: 1 - folder, 0 - file
def get_type(elem_id):
    logging.info('SQL - get_type func for %s' % elem_id)
    result = cur.execute("SELECT type FROM elements WHERE id = ?", (elem_id,)).fetchone()
    return result if not result else int(result[0])


# добавление нового элемента в базу данных и фиксация его изменения
# data - данные элемента, date - дата добавления
def add_item(data, date):
    logging.info('SQL - insert new data: %s %s' % (data, date))
    type_elem = 1 if data['type'] == 'FOLDER' else 0

    # добавляем файл на сервер в базу
    cur.execute("INSERT OR REPLACE INTO elements (id, url, date, parent, type, size) VALUES (?, ?, ?, ?, ?, ?)",
                (data['id'], data.get('url'), date, data['parentId'], type_elem, data.get('size')))

    # фиксируем изменение файла или его добавление в историю запросов
    cur.execute("INSERT INTO history (id_elem, url, date, parent, type, size) VALUES (?, ?, ?, ?, ?, ?)",
                (data['id'], data.get('url'), date, data['parentId'], type_elem, data.get('size')))
    con.commit()


# получение ссылки на файл по id
# elem_id - id файла
def get_url(elem_id):
    logging.info('SQL - get_url func for %s' % elem_id)
    result = cur.execute("SELECT url FROM elements WHERE id = ?", (elem_id,)).fetchone()
    return result if not result else result[0]


# получение id файла по ссылке на него
# elem_url - url файла
def get_id(elem_url):
    logging.info('SQL - get_id func for %s' % elem_url)
    result = cur.execute("SELECT id FROM elements WHERE url = ?", (elem_url,)).fetchone()
    return result if not result else result[0]


# функция, удаляющая элемент из базы
# elem_id - id удаляемого элемента
def del_item(elem_id):
    logging.info('SQL - delete item func for %s' % elem_id)
    cur.execute('DELETE FROM elements WHERE id = ?', (elem_id,))
    con.commit()


# функция, возвращающая список элементов в папке
# folder_id - id папки
def get_folder_files(folder_id):
    logging.info('SQL - get_folder_files func for %s' % folder_id)
    result = cur.execute('SELECT id FROM elements WHERE parent = ?', (folder_id,)).fetchall()
    return result


# функция, определяющая наличие элемента в базе
# elem_id - id проверяемого элемента
def check_id(elem_id):
    logging.info('SQL - check_id func for %s' % elem_id)
    if len(cur.execute("SELECT * FROM elements WHERE id = ?", (elem_id,)).fetchall()) == 1:
        return True
    return False


# функция, возвращающая размер файла
# file_id - id файла
def get_size(file_id):
    logging.info('SQL - get_size func for %s' % file_id)
    return cur.execute('SELECT size FROM elements WHERE id = ?', (file_id,)).fetchone()[0]


# функция, возвращающая данные элемента
# item_id - id элемента
def get_item(item_id):
    logging.info('SQL - get_item func for %s' % item_id)
    return cur.execute('SELECT * FROM elements WHERE id = ?', (item_id,)).fetchone()


# функция, обновляющая дату для папки
# для случаев, когда изменяется или добавляется новый файл
# folder_id - id папки, date - дата изменения
def update_date(folder_id, date):
    logging.info('SQL - update_date func for %s %s' % (folder_id, date))
    cur.execute('UPDATE elements SET date = ? WHERE id = ?', (date, folder_id))
    con.commit()


# функция, возврщающая родительскую папку элемента
# elem_id - id элемента
def get_parent(elem_id):
    logging.info('SQL - get_parent func for %s' % elem_id)
    result = cur.execute('SELECT parent FROM elements WHERE id = ?', (elem_id,)).fetchone()
    return result if not result else result[0]


# функция, возвращающая из базы файлы, который были обновленные в заданный период
# date_from - дата, полученная от пользователя
def get_files_updated(date_from):
    logging.info('SQL - get_files_updated func for %s' % date_from)
    return cur.execute('SELECT * FROM elements WHERE datetime(date) >= datetime(?, "-1 day") '
                       'AND datetime(date) <= datetime(?) AND type = 0', (date_from, date_from)).fetchall()
