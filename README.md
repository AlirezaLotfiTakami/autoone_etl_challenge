# AutoOne ETL Challenge
Although it was a simple project, I tried to use best practices OOP Design principle and patterns and Test Driven Development
in this project as a show case for my knowledge.
In the next parts I going to explain details of how to use the project and design and implementation.
## How to use it
You can easily install it using the following command:
```
git clone https://github.com/AlirezaLotfiTakami/autoone_etl_challenge.git
cd project-directory 
python setup.py install
```
Take a look at main.py file for how to use package API.
```python
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
    
```

In the above example at first we instantiate and run a pipeline and load the output in a python list.
After that we redefine that pipeline but change the loader module and load the output to a csv file.
So when you run main.py file by using below command 
```python
python main.py 
```
You can see the results that will printed on console also you will get a file that it's name is sample_out.txt in root directory of project. 
## Design
As mentioned in the project specification requirements often change. So we design a highly extendable architecture and 
we encapsulate different logic of ETL pipeline in different packages and the users can extend or alter every tiny part of 
system separately So it's rarely possible that a change somewhere in our code propagate this changes somewhere else.
At the end we have a easy to extend ETL pipeline that can extract data from csv file and transform it and then load it to 
a file or list in memory and it's really easy to extend it to extract or load for different sources like DB and transform 
different formats in a different order.

In this project we have four main module:

* Extractor: Every Extractor class have to implement BaseExtractor class.
Here we have used built-in iterator protocol of python so it's compatible with standard python
syntax 'for each' and we can easily iterate over extracted data.

* Transformer: Here we have two base classes. One of them is BaseColumnTransformer and the other one is BaseRowTransformer.
Column transformer classes are responsible for transforming each column data. They are general enough So they can be used 
for different cases. For example I used StringToIntegerTransformer class for converting both engine-size and weight data.
Column transformer classes accept an argument called field_name that specifies the name of field that should be found and 
transformed.Row transformer classes are specifying which column transformers participating in transforming a whole row.They also 
specify the order of results in the output of transformation.
Implementing a new row transformer class is very easy. For example to meet the requirement I had to implement a PricePredictionRowTransformer as below:
```python
class PricePredictionRowTransformer(BaseRowTransformer):
    transformer_list = [
        OneHotEncodingTransformer("engine-location", ["front", "rear"]),
        WordNumberToIntegerTransformer("num-of-cylinders"),
        StringToIntegerTransformer("engine-size"),
        StringToIntegerTransformer("weight"),
        StringToFloatTransformer("horsepower"),
        IsOrNotTransformer("aspiration", "turbo"),
        CentsToEuroTransformer("price"),
        IdenticalColumnTransformer("make")
    ]
```
As you can see it's very easy and you just need to override the transformer_list with those column transformer classes you want and 
in the same other that you want the output.
* Loader: Loader classes take the converted data from transformer and load those data to a output object like python list or
a csv file. Loader module is open for extend so different output formats can be supported. They just need to implement a new 
loader class and extend it from BaseLoaderClass.

* Pipeline: This class play a coordinator role in our design. It utilize extractor, transformer and loader classes and bind 
them together. Every time you want to used this system you need to instantiate a pipeline object and configure it with suitable
extractor, transformer and loader classes after that you can call 'run' method for running the pipeline.
For example in the below snippet we instantiate a Pipeline that exactly cover this challenge requirements.
```python
price_prediction_pipeline = Pipeline(CSVExtractor(sample_file_input),
                                         PricePredictionRowTransformer(),
                                         ListLoader())
result_list = price_prediction_pipeline.run()
print("The result is :".format(sample_file_input))
for item in result_list:
    print(item)
```

## Implementation
In designing I try to achieve an extendable architecture and to implementing that design I try to used most pythonic and principal way of implementation.
For example I used base abstract classes and methods everywhere it was possible. Also I took advantage of Test Driven Development (TDD) and the whole project is completely covered by unit testing.