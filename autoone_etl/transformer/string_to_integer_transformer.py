from autoone_etl.transformer.base_column_transformer import BaseColumnTransformer


class StringToIntegerTransformer(BaseColumnTransformer):

    def do(self, value):
        return int(value)
