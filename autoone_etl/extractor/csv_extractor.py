import csv

from autoone_etl.extractor.base_extractor import BaseExtractor


class CSVExtractor(BaseExtractor):
    def __init__(self, csv_file_path) -> None:
        super().__init__()
        self.csv_file = open(csv_file_path, newline='')
        self.reader = csv.reader(self.csv_file, delimiter=';', quotechar="'")
        self.header_list = self._read_headers()

    def _read_headers(self):
        header_list = list()
        next_row = self.reader.__next__()
        for col in next_row:
            if col:
                header_list.append(col)
            else:
                header_list.append("_row_number")
        return header_list

    def __next__(self):
        next_row = self.reader.__next__()
        row_dict = dict()
        for index, col_value in enumerate(next_row):
            col_key = self.header_list[index]
            row_dict[col_key] = col_value
        return row_dict

    def close(self):
        self.csv_file.close()
