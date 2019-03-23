from autoone_etl.test.transformer.base_transformer_test import BaseTransformerTest
from autoone_etl.transformer.word_number_to_integer_transformer import WordNumberToIntegerTransformer


class TestWordNumberToIntegerTransformer(BaseTransformerTest):

    def test_do(self):
        transformer = WordNumberToIntegerTransformer("field_name")
        input_value_list = ["four", "six",
                            "seven billion one hundred million thirty one thousand three hundred thirty seven"]
        expected_value_list = [4, 6, 7100031337]
        self.transformer_do_test(transformer, input_value_list, expected_value_list)
