import json
import yaml
import sys
import os

def format_atom(val):
    if isinstance(val, str):
        val = val.replace('"', '\\"')  # escape quotes
        return f'"{val}"'
    elif isinstance(val, bool):
        return "true" if val else "false"
    elif val is None:
        return "null"
    else:
        return str(val)

def to_sexpr(key, value):
    if isinstance(value, dict):
        parts = [to_sexpr(f"yaml:{k}", v) for k, v in value.items()]
        return f"({key} {' '.join(parts)})"
    elif isinstance(value, list):
        items = [to_sexpr("yaml:item", v) for v in value]
        return f"({key} {' '.join(items)})"
    else:
        return f"({key} {format_atom(value)})"

def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        if file_path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        elif file_path.endswith('.json'):
            return json.load(f)
        else:
            raise ValueError("Unsupported file type. Use .yaml, .yml, or .json")

def main(file_path):
    data = read_input_file(file_path)
    sexpr = to_sexpr("yaml", data)
    print(sexpr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python yaml_to_sexpr.py <file.yaml|file.json>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    main(file_path)
