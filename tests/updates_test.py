'''
Тесты, проверяющие /updates на различных входных данных
'''

from test_data.data import UPDATES_VALID_RESPONSE, IMPORT_VALID_DATA, UPDATES_VALID_DATA
from unit_test import request as req, deep_sort_children, print_diff
from import_test import test_import_valid
import urllib
import sys


def updates_test(date, i):
    params = urllib.parse.urlencode({
        "date": date
    })

    status, response = req(f"/updates?{params}", json_response=True)
    assert status == 200, f"Expected HTTP status code 200, got {status}"

    deep_sort_children(response)
    deep_sort_children(UPDATES_VALID_RESPONSE[i])
    if response != UPDATES_VALID_RESPONSE[i]:
        print_diff(UPDATES_VALID_RESPONSE[i], response)
        print("Response tree doesn't match expected tree.")
        sys.exit(1)

    print(f"Test nodes for {date} passed.")


def main():
    test_import_valid(IMPORT_VALID_DATA)
    for i in range(len(UPDATES_VALID_DATA)):
        updates_test(UPDATES_VALID_DATA[i], i)


if __name__ == "__main__":
    main()
