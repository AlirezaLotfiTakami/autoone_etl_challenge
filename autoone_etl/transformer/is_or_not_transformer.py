from autoone_etl.transformer.base_column_transformer import BaseColumnTransformer


class IsOrNotTransformer(BaseColumnTransformer):

    def __init__(self, column_name, match_value) -> None:
        super().__init__(column_name)
        self.match_value = match_value

    def do(self, value):
        if value == self.match_value:
            return 1
        return 0
