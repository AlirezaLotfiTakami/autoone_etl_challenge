class Pipeline:

    def __init__(self, extractor, transformer, loader) -> None:
        super().__init__()
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        for row in self.extractor:
            transformed_row = self.transformer.transform(row)
            # check if this row should be ignored because of NA occurrence
            if transformed_row:
                self.loader.load_next(transformed_row)
        result = self.loader.get_results()
        # cleaning things up
        self.extractor.close()
        self.loader.close()
        return result
