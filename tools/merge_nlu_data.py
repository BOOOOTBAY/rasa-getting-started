from __future__ import annotations

from typing import List
import os
import json
from collections import defaultdict

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from tools.config import root_dir


def merge_nlu_json_file(files: List[str], target_file: str):
    """merge nlu file to the target file

    Args:
        files (List[str]): json nlu files
        target_file (str): the output nlu files
    """
    # 1. define the final nlu result
    nlu_data = defaultdict(list)

    # 2. read & load json file
    for file in files:
        with open(file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data = data['rasa_nlu_data']
            nlu_data['examples'].extend(data['common_examples'])
            nlu_data['regex_features'].extend(data['regex_features'])
            nlu_data['entity_synonyms'].extend(data['entity_synonyms'])
    
    # 3. save result to the target file
    with open(target_file, 'w+', encoding='utf-8') as f:
        json.dump(dict(rasa_nlu_data=nlu_data), f, ensure_ascii=False)


def merge_nlu_data():
    # 1. define the data variables
    nlu_dir = './data/nlu'
    target_file = './data/nlu.json'

    # 2. load nlu files
    nlu_files = []
    for file in os.listdir(os.path.join(nlu_dir)):
        nlu_files.append(os.path.join(root_dir, nlu_dir, file))
    
    
    merge_nlu_json_file(
        nlu_files,
        os.path.join(root_dir, target_file)
    )

if __name__ == '__main__':
    merge_nlu_data()