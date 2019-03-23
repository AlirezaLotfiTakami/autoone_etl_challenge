from autoone_etl.transformer.base_column_transformer import BaseColumnTransformer


class CentsToEuroTransformer(BaseColumnTransformer):

    def do(self, value):
        cents = int(value)
        return cents / 100

