import csv
import json

with open("D:\\coding\\Python\\voice_assistant\\tuning_data.csv", 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    with open('tuning_data.jsonl', 'w', encoding='utf-8') as jsonlfile:
        for row in reader:
            json.dump(row, jsonlfile, ensure_ascii=False)
            jsonlfile.write('\n')

print("JSONL file 'tuning_data.jsonl' created successfully.")