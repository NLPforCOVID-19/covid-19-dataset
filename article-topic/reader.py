import os
import sys
import json

dataset_jsonl ='./article_topic_dataset.jsonl'
decoder = json.JSONDecoder()

with open(dataset_jsonl, "r") as f:
    json_lines = f.readlines()
    for json_line in json_lines:
        line = decoder.raw_decode(json_line.strip())[0]
        for (k, v) in line.items():
            print (k, v)
        break

