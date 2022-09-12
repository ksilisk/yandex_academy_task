'''
Тесты, проверяющие /import на различных входных данных
Сначала прогоняются валидные данные
Потом проверяется валидация на примере невалидных входных значений
'''

from test_data.data import IMPORT_VALID_DATA, IMPORT_INVALID_DATA
from unit_test import request as req


def test_import_valid(data):
    for index, batch in enumerate(data):
        print(f"Importing valid batch {index}")
        status, _ = req("/imports", method="POST", data=batch)

        assert status == 200, f"Expected HTTP status code 200, got {status}"

    print("Test import valid data passed.")


def test_import_invalid(data):
    for index, batch in enumerate(data):
        print(f"Importing invalid batch {index}")
        status, _ = req("/imports", method="POST", data=batch)

        assert status == 400, f"Expected HTTP status code 400, got {status}"

    print("Test import invalid data passed.")


def main():
    test_import_valid(IMPORT_VALID_DATA)
    test_import_invalid(IMPORT_INVALID_DATA)


if __name__ == "__main__":
    main()
