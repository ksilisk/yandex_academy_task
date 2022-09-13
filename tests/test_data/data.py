'''
Тут хранятся все данные для тестирования
'''

API_BASEURL = "http://0.0.0.0:80"

IMPORT_VALID_DATA = [
    {
        "items": [
            {
                "type": "FOLDER",
                "id": "1",
                "parentId": None
            }
        ],
        "updateDate": "2022-02-01T12:00:00Z"
    },
    {
        "items": [
            {
                "type": "FILE",
                "url": "files/f2",
                "id": "2",
                "size": 10,
                "parentId": "1"
            },
            {
                "type": "FILE",
                "url": "files/f3",
                "id": "3",
                "size": 25,
                "parentId": None
            },
            {
                "type": "FOLDER",
                "id": "4",
                "parentId": "1"
            }

        ],
        "updateDate": "2022-02-01T14:00:00Z"
    },
    {
        "items": [
            {
                "type": "FILE",
                "url": "files/f5",
                "id": "5",
                "size": 14,
                "parentId": "4"
            },
            {
                "type": "FILE",
                "url": "files/f6",
                "id": "6",
                "size": 546,
                "parentId": None
            },
            {
                "type": "FOLDER",
                "id": "7",
                "parentId": None
            },
            {
                "type": "FOLDER",
                "id": "8",
                "parentId": "4"
            }
        ],
        "updateDate": "2022-02-01T19:00:00Z"
    }
]

IMPORT_INVALID_DATA = [

    # проверка отсутствия элементов
    {
        "updateDate": "2022-02-01T20:00:00Z"
    },

    # проверка отсутствия даты
    {
        "items": [
            {
                "type": "FOLDER",
                "id": "8",
                "parentId": None
            }
        ]
    },

    # проверка на смену типа элемента (с папки на файл)
    {
        "items": [
            {
                "type": "FILE",
                "id": "1",
                "url": "files/f9",
                "size": 78,
                "parentId": None
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на смену типа элемента (с файла на папку)
    {
        "items": [
            {
                "type": "FOLDER",
                "id": "2",
                "parentId": None
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на то, что ссылка уже занята другим файлом
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "url": "files/f2",
                "size": 789,
                "parentId": None
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на валидность размера файла
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "url": "files/f9",
                "size": "789",
                "parentId": None
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка родителя на то, что это папка
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "url": "files/f9",
                "size": 789,
                "parentId": "2"
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на наличие родительской папки в базе
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "url": "files/f9",
                "size": 789,
                "parentId": "10"
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на недостающие данные
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "parentId": None
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на отсутствие ссылки на файл
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "url": None,
                "size": 789,
                "parentId": None
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на размер файла ( > 0)
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "url": "files/f9",
                "size": 0,
                "parentId": None
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на валидность id родителя
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "url": "files/f9",
                "size": 789,
                "parentId": 78
            }
        ],
        "updateDate": "2022-02-02T20:00:00Z"
    },

    # проверка на валидность даты
    {
        "items": [
            {
                "type": "FILE",
                "id": "9",
                "url": "files/f9",
                "size": 789,
                "parentId": None
            }
        ],
        "updateDate": "2022-02-0220:00:00Z"
    }
]

NODES_VALID_RESPONSE = [

    # проверка команды для элемента с id = 1
    {
        "type": "FOLDER",
        "id": "1",
        "url": None,
        "size": 24,
        "parentId": None,
        "date": "2022-02-01T19:00:00Z",
        "children": [
            {
                "type": "FOLDER",
                "id": "4",
                "size": 14,
                "url": None,
                "parentId": "1",
                "date": "2022-02-01T19:00:00Z",
                "children": [
                    {
                        "type": "FOLDER",
                        "id": "8",
                        "size": 0,
                        "url": None,
                        "parentId": "4",
                        "date": "2022-02-01T19:00:00Z",
                        "children": []
                    },
                    {
                        "type": "FILE",
                        "id": "5",
                        "url": "files/f5",
                        "size": 14,
                        "date": "2022-02-01T19:00:00Z",
                        "parentId": "4",
                        "children": None
                    }
                ]
            },
            {
                "type": "FILE",
                "id": "2",
                "url": "files/f2",
                "size": 10,
                "date": "2022-02-01T14:00:00Z",
                "parentId": "1",
                "children": None
            }
        ]
    },

    # проверка команды для элемента с id = 8
    {
        "type": "FOLDER",
        "id": "8",
        "url": None,
        "size": 0,
        "date": "2022-02-01T19:00:00Z",
        "parentId": "4",
        "children": []
    },

    # проверка команды для элемента с id = 4
    {
        "type": "FOLDER",
        "id": "4",
        "size": 14,
        "url": None,
        "parentId": "1",
        "date": "2022-02-01T19:00:00Z",
        "children": [
            {
                "type": "FOLDER",
                "id": "8",
                "size": 0,
                "url": None,
                "parentId": "4",
                "date": "2022-02-01T19:00:00Z",
                "children": []
            },
            {
                "type": "FILE",
                "id": "5",
                "url": "files/f5",
                "size": 14,
                "date": "2022-02-01T19:00:00Z",
                "parentId": "4",
                "children": None
            }
        ]
    },

    # проверка команды для элемента с id = 6
    {
        "type": "FILE",
        "id": "6",
        "size": 546,
        "url": "files/f6",
        "date": "2022-02-01T19:00:00Z",
        "parentId": None,
        "children": None
    },

    # проверка команды для элемента с id = 5
    {
        "type": "FILE",
        "id": "5",
        "url": "files/f5",
        "size": 14,
        "date": "2022-02-01T19:00:00Z",
        "parentId": "4",
        "children": None
    }
]

DELETE_DATA = {
    "4": ["4", "5", "8"],
    "1": ["1", "2"],
    "6": ["6"],
    "7": ["7"],
    "3": ["3"]
}

UPDATES_VALID_DATA = [
    "2022-02-01T14:00:00Z",
    "2022-02-01T19:00:00Z"
]

UPDATES_VALID_RESPONSE = [
    {
        "items": [
            {
                "type": "FILE",
                "url": "files/f2",
                "id": "2",
                "date": "2022-02-01T14:00:00Z",
                "size": 10,
                "parentId": "1"
            },
            {
                "type": "FILE",
                "url": "files/f3",
                "id": "3",
                "date": "2022-02-01T14:00:00Z",
                "size": 25,
                "parentId": None
            }
        ]
    },
    {
        "items": [
            {
                "type": "FILE",
                "url": "files/f2",
                "id": "2",
                "date": "2022-02-01T14:00:00Z",
                "size": 10,
                "parentId": "1"
            },
            {
                "type": "FILE",
                "url": "files/f3",
                "id": "3",
                "date": "2022-02-01T14:00:00Z",
                "size": 25,
                "parentId": None
            },
            {
                "type": "FILE",
                "url": "files/f5",
                "id": "5",
                "date": "2022-02-01T19:00:00Z",
                "size": 14,
                "parentId": "4"
            },
            {
                "type": "FILE",
                "url": "files/f6",
                "id": "6",
                "date": "2022-02-01T19:00:00Z",
                "size": 546,
                "parentId": None
            }

        ]
    }
]
