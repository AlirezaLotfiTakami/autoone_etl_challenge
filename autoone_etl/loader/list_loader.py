from autoone_etl.loader.base_loader import BaseLoader


class ListLoader(BaseLoader):
    def __init__(self) -> None:
        super().__init__()
        self.result_list = list()
        self.header_list = None

    def load_next(self, data):
        if not self.header_list:
            self.header_list = list(data.keys())
            self.result_list.append(self.header_list)
        self.result_list.append(list(data.values()))

    def get_results(self):
        return self.result_list

    def close(self):
        # a memory data structure doesn't need to be closed
        pass
