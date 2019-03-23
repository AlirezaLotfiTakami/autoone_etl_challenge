from autoone_etl.test.transformer.base_transformer_test import BaseTransformerTest
from autoone_etl.transformer.string_to_float_transformer import StringToFloatTransformer
from autoone_etl.transformer.word_number_to_integer_transformer import WordNumberToIntegerTransformer


class TestStringToFloatTransformer(BaseTransformerTest):

    def test_do(self):
        transformer = StringToFloatTransformer("field_name")
        input_value_list = ["123,456", "32,4", "27", "67856,2"]
        expected_value_list = [123.456, 32.4, 27, 67856.2]
        self.transformer_do_test(transformer, input_value_list, expected_value_list)
