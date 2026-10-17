#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(input):
    """convert files from CSV to JSON format"""
    try:
        with open(input, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except (FileNotFoundError, PermissionError, csv.Error, OSError):
        return False
