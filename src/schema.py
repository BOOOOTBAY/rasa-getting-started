from __future__ import annotations

from typing import List
import os
import json
from collections import defaultdict

from dataclasses import dataclass
from dataclasses_json import dataclass_json

def merge_nlu_json_file(files: List[str], target_file: str):
    """merge nlu file to the target file

    Args:
        files (List[str]): json nlu files
        target_file (str): the output nlu files
    """
    # 1. define the final nlu result
    examples = defaultdict(list)
    regex_features = defaultdict(list)
    entity_synonyms = defaultdict(list)    

    # 2. read & load json file
    for file in files:
        with open(file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            nlu_data = data['rasa_nlu_data']
            examples.extend(nlu_data['common_examples'])
            regex_features.extend(nlu_data['regex_features'])
            entity_synonyms.extend(nlu_data['entity_synonyms'])
    
    # 3. save result to the target file
    with open(target_file, 'w+', encoding='utf-8') as f:
        nlu_data = dict(common_examples=examples, regex_features=regex_features, entity_synonyms=entity_synonyms)
        json.dump(dict(rasa_nlu_data=nlu_data), f, ensure_ascii=False)