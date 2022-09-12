'''
Тесты проверяющие работоспособность /delete на различных входных данных
'''

from test_data.data import IMPORT_VALID_DATA, DELETE_DATA
from import_test import test_import_valid
from unit_test import request as req
import urllib


def check_node(node_id):
    status, _ = req(f"/nodes/{node_id}", json_response=True)
    assert status == 404, f"Expected HTTP status code 404, got {status}"


def delete_node(root_id, ids_for_check):
    params = urllib.parse.urlencode({
        "date": "2022-02-04T00:00:00Z"
    })

    status, _ = req(f"/delete/{root_id}?{params}", method="DELETE")
    assert status == 200, f"Expected HTTP status code 200, got {status}"

    for i in range(len(ids_for_check)):
        check_node(ids_for_check[i])

    print(f"Test delete for {root_id} passed")


def main():
    test_import_valid(IMPORT_VALID_DATA)
    for key, value in DELETE_DATA.items():
        delete_node(key, value)


if __name__ == "__main__":
    main()
