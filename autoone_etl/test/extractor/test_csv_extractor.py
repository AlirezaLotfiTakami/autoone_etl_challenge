from unittest import TestCase

from autoone_etl.extractor.csv_extractor import CSVExtractor


class TestCSVExtractor(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_result = [
            {'_row_number': '0', 'aspiration': 'std', 'body-style': 'convertible', 'bore': '3.47', 'city-mpg': '21',
             'compression-ratio': '9.00', 'curb-weight': '2548', 'drive-wheels': 'rwd', 'engine-location': 'front',
             'engine-size': '130', 'engine-type': 'dohc', 'fuel-system': 'mpfi', 'fuel-type': 'gas', 'height': '48.80',
             'highway-mpg': '27', 'horsepower': '111,03', 'length': '168.80', 'make': 'alfa-romero',
             'normalized-losses': '-', 'num-of-cylinders': 'four', 'num-of-doors': 'two', 'peak-rpm': '5000',
             'price': '1349500', 'stroke': '2.68', 'weight': '3', 'wheel-base': '88.60', 'width': '64.10'},
            {'_row_number': '1', 'aspiration': 'std', 'body-style': 'convertible', 'bore': '3.47', 'city-mpg': '21',
             'compression-ratio': '9.00', 'curb-weight': '2548', 'drive-wheels': 'rwd', 'engine-location': 'front',
             'engine-size': '130', 'engine-type': 'dohc', 'fuel-system': 'mpfi', 'fuel-type': 'gas', 'height': '48.80',
             'highway-mpg': '27', 'horsepower': '111,73', 'length': '168.80', 'make': 'alfa-romero',
             'normalized-losses': '-', 'num-of-cylinders': '-', 'num-of-doors': 'two', 'peak-rpm': '5000',
             'price': '1650000', 'stroke': '2.68', 'weight': '3', 'wheel-base': '88.60', 'width': '64.10'}]

    def test_extract(self):
        test_file_path = "../sample_file/short_sample_input.txt"
        extractor = CSVExtractor(test_file_path)
        result_list = list(extractor)
        self.assertListEqual(self.expected_result, result_list)
        extractor.close()
