from unittest import TestCase

from autoone_etl.loader.list_loader import ListLoader


class TestListLoader(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.input_list = [
            {'_row_number': '1', 'aspiration': 'std', 'body-style': 'convertible', 'bore': '3.47', 'city-mpg': '21',
             'compression-ratio': '9.00', 'curb-weight': '2548', 'drive-wheels': 'rwd', 'engine-location': 'front',
             'engine-size': '130', 'engine-type': 'dohc', 'fuel-system': 'mpfi', 'fuel-type': 'gas', 'height': '48.80',
             'highway-mpg': '27', 'horsepower': '111,73', 'length': '168.80', 'make': 'alfa-romero',
             'normalized-losses': '-', 'num-of-cylinders': '-', 'num-of-doors': 'two', 'peak-rpm': '5000',
             'price': '1650000', 'stroke': '2.68', 'weight': '3', 'wheel-base': '88.60', 'width': '64.10'}]
        cls.expected_list = [
            ['_row_number', 'aspiration', 'body-style', 'bore', 'city-mpg',
             'compression-ratio', 'curb-weight', 'drive-wheels', 'engine-location',
             'engine-size', 'engine-type', 'fuel-system', 'fuel-type', 'height',
             'highway-mpg', 'horsepower', 'length', 'make',
             'normalized-losses', 'num-of-cylinders', 'num-of-doors', 'peak-rpm',
             'price', 'stroke', 'weight', 'wheel-base', 'width'],
            ['1', 'std', 'convertible', '3.47', '21',
             '9.00', '2548', 'rwd', 'front',
             '130', 'dohc', 'mpfi', 'gas', '48.80',
             '27', '111,73', '168.80', 'alfa-romero',
             '-', '-', 'two', '5000',
             '1650000', '2.68', '3', '88.60', '64.10']]

    def test_load(self):
        loader = ListLoader()
        for item in self.input_list:
            loader.load_next(item)
        self.assertListEqual(self.expected_list, loader.get_results())
