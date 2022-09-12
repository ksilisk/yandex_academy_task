'''
Тесты, проверяющие работоспособность /nodes на различных входных данных
'''

from unit_test import request as req, deep_sort_children, print_diff
from test_data.data import NODES_VALID_RESPONSE, IMPORT_VALID_DATA
from import_test import test_import_valid
import sys


def nodes_test(root_id, i):
    status, response = req(f"/nodes/{root_id}", json_response=True)
    assert status == 200, f"Expected HTTP status code 200, got {status}"

    deep_sort_children(response)
    deep_sort_children(NODES_VALID_RESPONSE[i])
    if response != NODES_VALID_RESPONSE[i]:
        print_diff(NODES_VALID_RESPONSE[i], response)
        print("Response tree doesn't match expected tree.")
        sys.exit(1)

    print(f"Test nodes for {root_id} passed.")


def main():
    test_import_valid(IMPORT_VALID_DATA)
    nodes = ["1", "8", "4", "6", "5"]
    for i in range(len(nodes)):
        nodes_test(nodes[i], i)


if __name__ == "__main__":
    main()
