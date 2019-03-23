import csv

from autoone_etl.loader.base_loader import BaseLoader


class CSVLoader(BaseLoader):
    def __init__(self, csv_file_path) -> None:
        super().__init__()
        self.header_list = None
        self.csv_file_path = csv_file_path
        self.csv_file = open(csv_file_path, 'w', newline='')
        self.writer = csv.writer(self.csv_file, delimiter=';',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)

    def load_next(self, data):
        if not self.header_list:
            self.header_list = list(data.keys())
            self.writer.writerow(self.header_list)
        self.writer.writerow(list(data.values()))

    def get_results(self):
        return self.csv_file_path

    def close(self):
        self.csv_file.close()
