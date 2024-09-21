from Src.Core.validator import validator
from Src.Core.base_models import base_model_code
from Src.Models.range import range_model
from Src.Models.nomenclature import nomenclature_model

class Ingredient(base_model_code):
    def __init__(self, nomenclature: nomenclature_model, measured_amount: range_model):
        super().__init__()

        self._nomenclature = None
        self._measured_amount = None

        self.nomenclature = nomenclature
        self.measured_amount = measured_amount

    @property
    def nomenclature(self) -> nomenclature_model:
        return self._nomenclature

    @nomenclature.setter
    def nomenclature(self, value: nomenclature_model):
        validator.validate(value, nomenclature_model)
        self._nomenclature = value

    @property
    def measured_amount(self) -> range_model:
        return self._measured_amount

    @measured_amount.setter
    def measured_amount(self, value: range_model):
        validator.validate(value, range_model)
        self._measured_amount = value
