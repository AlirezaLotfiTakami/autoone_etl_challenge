from autoone_etl.transformer.base_column_transformer import BaseColumnTransformer
from autoone_etl.util.one_hot_encoding import one_hot_encode


class OneHotEncodingTransformer(BaseColumnTransformer):

    def __init__(self, column_name, category_list) -> None:
        super().__init__(column_name)
        self.category_list = category_list

    def do(self, value):
        return one_hot_encode(value, self.category_list)
