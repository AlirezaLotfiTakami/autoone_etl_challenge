from abc import ABC


class BaseRowTransformer(ABC):
    transformer_list = None

    def __init__(self) -> None:
        super().__init__()

    def transform(self, row):
        if not self.transformer_list:
            raise Exception("Transform list in empty")
        result_dict = dict()
        for transformer in self.transformer_list:
            transformation_result = transformer.transform(row)
            # it means one of the columns value in this row is NA
            if not transformation_result:
                return None
            result_dict.update(transformation_result)
        return result_dict
