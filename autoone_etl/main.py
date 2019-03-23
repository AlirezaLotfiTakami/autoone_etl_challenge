from autoone_etl.extractor.csv_extractor import CSVExtractor
from autoone_etl.loader.csv_loader import CSVLoader
from autoone_etl.loader.list_loader import ListLoader
from autoone_etl.pipeline.pipeline import Pipeline
from autoone_etl.transformer.price_prediction_row_transformer import PricePredictionRowTransformer

if __name__ == "__main__":
    sample_file_input = "test/sample_file/sample_input.txt"
    print("Extracting and Transforming from file {} and loading to python list data structure.".format(sample_file_input))
    price_prediction_pipeline = Pipeline(CSVExtractor(sample_file_input),
                                         PricePredictionRowTransformer(),
                                         ListLoader())
    result_list = price_prediction_pipeline.run()
    print("The result is :".format(sample_file_input))
    for item in result_list:
        print(item)

    output_csv_file = "sample_out.txt"
    print("Extracting and Transforming from file {} and loading to file {} .".format(sample_file_input,output_csv_file))
    price_prediction_pipeline_to_file = Pipeline(CSVExtractor(sample_file_input),
                                                 PricePredictionRowTransformer(),
                                                 CSVLoader(output_csv_file))
    result_list = price_prediction_pipeline_to_file.run()
    print("Take a look at {} !".format(output_csv_file))
