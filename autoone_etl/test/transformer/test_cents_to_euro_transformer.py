from autoone_etl.test.transformer.base_transformer_test import BaseTransformerTest
from autoone_etl.transformer.cents_to_euro_transformer import CentsToEuroTransformer
from autoone_etl.transformer.is_or_not_transformer import IsOrNotTransformer


class TestWordNumberToIntegerTransformer(BaseTransformerTest):

    def test_do(self):
        transformer = CentsToEuroTransformer("field_name")
        input_value_list = ["1", "100", "153", "345897"]
        expected_value_list = [0.01, 1, 1.53, 3458.97]
        self.transformer_do_test(transformer, input_value_list, expected_value_list)
