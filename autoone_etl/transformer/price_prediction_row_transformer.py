from autoone_etl.transformer.base_row_transformer import BaseRowTransformer
from autoone_etl.transformer.cents_to_euro_transformer import CentsToEuroTransformer
from autoone_etl.transformer.identical_column_transformer import IdenticalColumnTransformer
from autoone_etl.transformer.is_or_not_transformer import IsOrNotTransformer
from autoone_etl.transformer.one_hot_encoding_transformer import OneHotEncodingTransformer
from autoone_etl.transformer.string_to_float_transformer import StringToFloatTransformer
from autoone_etl.transformer.string_to_integer_transformer import StringToIntegerTransformer
from autoone_etl.transformer.word_number_to_integer_transformer import WordNumberToIntegerTransformer


class PricePredictionRowTransformer(BaseRowTransformer):
    transformer_list = [
        OneHotEncodingTransformer("engine-location", ["front", "rear"]),
        WordNumberToIntegerTransformer("num-of-cylinders"),
        StringToIntegerTransformer("engine-size"),
        StringToIntegerTransformer("weight"),
        StringToFloatTransformer("horsepower"),
        IsOrNotTransformer("aspiration", "turbo"),
        CentsToEuroTransformer("price"),
        IdenticalColumnTransformer("make")
    ]
