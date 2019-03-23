from unittest import TestCase


class BaseTransformerTest(TestCase):

    def transformer_do_test(self, transformer, input_value_list, expected_value_list):
        for index, input_value in enumerate(input_value_list):
            result = transformer.do(input_value)
            expected_value = expected_value_list[index]
            self.assertEqual(expected_value, result,
                             "expected value is {} but given value is {}".format(expected_value, result))
