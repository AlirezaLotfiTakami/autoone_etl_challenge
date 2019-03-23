from autoone_etl.transformer.base_column_transformer import BaseColumnTransformer
from locale import *


class StringToFloatTransformer(BaseColumnTransformer):

    def do(self, value):
        setlocale(LC_NUMERIC, 'german_germany')
        result = atof(value)
        setlocale(LC_NUMERIC, '')
        return result
