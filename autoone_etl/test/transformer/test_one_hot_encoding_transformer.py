from autoone_etl.test.transformer.base_transformer_test import BaseTransformerTest
from autoone_etl.transformer.is_or_not_transformer import IsOrNotTransformer
from autoone_etl.transformer.one_hot_encoding_transformer import OneHotEncodingTransformer


class TestOneHotEncodingTransformer(BaseTransformerTest):

    def test_do(self):
        transformer = OneHotEncodingTransformer("field_name", ["front", "rear", "right", "left"])
        input_value_list = ["front", "rear", "right", "left"]
        expected_value_list = [1, 2, 4, 8]
        self.transformer_do_test(transformer, input_value_list, expected_value_list)
