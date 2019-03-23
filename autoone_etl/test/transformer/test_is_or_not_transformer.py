from autoone_etl.test.transformer.base_transformer_test import BaseTransformerTest
from autoone_etl.transformer.is_or_not_transformer import IsOrNotTransformer


class TestIsOrNotTransformer(BaseTransformerTest):

    def test_do(self):
        transformer = IsOrNotTransformer("field_name", "turbo")
        input_value_list = ["turbo", "std", "nothing", "something"]
        expected_value_list = [1, 0, 0, 0]
        self.transformer_do_test(transformer, input_value_list, expected_value_list)
