from abc import abstractmethod, ABC


class BaseColumnTransformer(ABC):

    def __init__(self, column_name) -> None:
        super().__init__()
        self.column_name = column_name

    def transform(self, row):
        value = self.find(row)
        if self._is_na(value):
            return None
        transformed_value = self.do(value)
        return {
            self.column_name: transformed_value
        }

    def _is_na(self, value):
        return value.replace(" ", "") == "-"

    def find(self, row):
        column_value = row.get(self.column_name, None)
        if not column_value:
            raise Exception("column {} not found !".format(self.column_name))
        return column_value

    @abstractmethod
    def do(self, value):
        pass
