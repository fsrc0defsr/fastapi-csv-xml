import os
from typing import List

def generate_xml(data: List[dict], file_name: str) -> None:
    is_new_file = not os.path.exists(file_name)

    with open(file_name, 'a') as f:
        if is_new_file:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<data>\n')
        for item in data:
            f.write('    <record>\n')
            for key, value in item.items():
                f.write(f'        <{key}>{value}</{key}>\n')
            f.write('    </record>\n')
        if is_new_file:
            f.write('</data>')

    print(f"Data appended to {file_name}")
