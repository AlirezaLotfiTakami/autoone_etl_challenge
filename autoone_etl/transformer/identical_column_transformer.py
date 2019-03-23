from autoone_etl.transformer.base_column_transformer import BaseColumnTransformer


class IdenticalColumnTransformer(BaseColumnTransformer):

    def do(self, value):
        return value
