from Src.Models.nomenclature import nomenclature_model
from Src.Core.validator import validator
import datetime

class recipe_model:
    def __init__(self, name: str = '', cooking_time: datetime.timedelta = None,
                 ingredients: list[nomenclature_model] = None, cooking_steps: list[str] = None):
        self._name = ''
        self._cooking_time = None
        self._ingredients = []
        self._cooking_steps = []

        self.name = name
        self.cooking_time = cooking_time
        self.ingredients = ingredients or []
        self.cooking_steps = cooking_steps or []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        validator.validate(value, str)
        self._name = value

    @property
    def cooking_time(self) -> datetime.timedelta | None:
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, value: datetime.timedelta):
        validator.validate(value, datetime.timedelta)
        self._cooking_time = value

    @property
    def ingredients(self) -> list[nomenclature_model]:
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value: list[nomenclature_model]):
        validator.validate(value, list)
        self._ingredients = value

    @property
    def cooking_steps(self) -> list[str]:
        return self._cooking_steps

    @cooking_steps.setter
    def cooking_steps(self, value: list[str]):
        validator.validate(value, list)
        self._cooking_steps = value
