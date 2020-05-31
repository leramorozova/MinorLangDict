import csv
import json
import os

from typing import Dict, List
from collections import OrderedDict

from pipline_utils import exceptions as exc


class DataGenerator:
    _REQUIRED_FIELDS = ["id"]
    _FORBIDDEN_TABLE_VALUES = ["", "-"]
    _FRAMEWORK_PATH = os.path.join("..", "framework")

    def __init__(self, path_to_csv: str, path_to_config: str, output_path: str):
        self._path_to_csv = path_to_csv
        self._output_path = output_path
        self._config: json = self._read_config(path_to_config)
        self.data: List[Dict[str, str]] = []

    @staticmethod
    def check_required_fields(config: json):
        for field in DataGenerator._REQUIRED_FIELDS:
            if field not in config:
                raise exc.ConfigError(field)

    @staticmethod
    def _read_config(path_to_json: str) -> json:
        with open(path_to_json, "r", encoding="UTF-8") as jsonfile:
            config = json.load(jsonfile)
            jsonfile.close()
        return config

    @staticmethod
    def _get_column_value(row: OrderedDict, fields: List[str]):
        values = [row.get(field, '') for field in fields if row.get(field, '') not in DataGenerator._REQUIRED_FIELDS]
        return ", ".join(values)

    def _process_word_entry(self, row: OrderedDict):
        for field in DataGenerator._REQUIRED_FIELDS:
            if field not in row:
                return
        word_entry = {field: self._get_column_value(row, self._config[field]) for field in self._config}
        self.data.append(word_entry)

    def _save_files(self):
        return

    def makefile(self):
        with open(self._path_to_csv, "r", encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self._process_word_entry(row)
        self._save_files()


if __name__ == "__main__":
    data_gen = DataGenerator("/home/valeria/Загрузки/lexcauc-concepts-tukita - concepts.csv",
                             "/home/valeria/git_projects/MinorLangDict/config.json")
    data_gen.makefile()