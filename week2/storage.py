import os
import tempfile
import argparse
import json

def get_storage_file_path() -> str:
    return os.path.join(tempfile.gettempdir(), 'storage.data')

def clear():
    file_path = get_storage_file_path()
    os.remove(file_path)

def save_to_file(dictionary: dict):
    file_path = get_storage_file_path()
    with open(file_path, 'w') as fp:
        json.dump(dictionary, fp, indent=4)


def read_from_file() -> dict:
    file_path = get_storage_file_path()
    if not os.path.isfile(file_path):
        return dict()

    with open(file_path, 'r') as fp:
        dictionary = json.load(fp)

    return dictionary

def read_from_file_with_checks():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

        return {}

def add_value(dictionary: dict, key: str, value: str):
    if key not in dictionary:
        dictionary[key] = []

    values = dictionary[key]
    values.append(value)

def get_value(dictionary: dict, key: str) -> list:
    if key not in dictionary:
        return []

    return dictionary[key]


parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key to set or to find")
parser.add_argument("--val", help="value to set")
parser.add_argument('--clear', action='store_true', help='Clear')

args = parser.parse_args()

if args.clear:
    clear()
    exit(0)

if not args.key:
    print("Please transfer a key")
    exit(1)


storage_dict = read_from_file()
if args.val:
    add_value(storage_dict, args.key, args.val)
    save_to_file(storage_dict)
else:
    value_list = get_value(storage_dict, args.key)
    print(", ".join(value_list))

