from unittest import TestCase

from autoone_etl.extractor.csv_extractor import CSVExtractor
from autoone_etl.loader.list_loader import ListLoader
from autoone_etl.pipeline.pipeline import Pipeline
from autoone_etl.transformer.price_prediction_row_transformer import PricePredictionRowTransformer


class TestPipeline(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.expected_list = [
            ['engine-location', 'num-of-cylinders', 'engine-size', 'weight', 'horsepower', 'aspiration', 'price',
             'make'], [1, 4, 130, 3, 111.03, 0, 13495.0, 'alfa-romero']]

    def test_run(self):
        price_prediction_pipeline = Pipeline(CSVExtractor("../sample_file/short_sample_input.txt"),
                                             PricePredictionRowTransformer(),
                                             ListLoader())
        result_list = price_prediction_pipeline.run()
        print(result_list)
        print(self.expected_list)
