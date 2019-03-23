from autoone_etl.test.transformer.base_transformer_test import BaseTransformerTest
from autoone_etl.transformer.string_to_integer_transformer import StringToIntegerTransformer


class TestStringToIntegerTransformer(BaseTransformerTest):

    def test_do(self):
        transformer = StringToIntegerTransformer("field_name")
        input_value_list = ["1", "6", "12", "36", "3232"]
        expected_value_list = [1, 6, 12, 36, 3232]
        self.transformer_do_test(transformer, input_value_list, expected_value_list)
