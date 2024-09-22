from Src.Core.base_models import base_model_name
from Src.Core.validator import validator

"""
Модель единицы измерения
"""
class range_model(base_model_name):
    __value:int = 1
    __base:'range' = None

    """
    Значение 
    """
    @property
    def value(self) -> int:
        return self.__value
    
    @value.setter
    def value(self, value: int):
        validator.validate(value, int)
        self.__value = value


    """
    Базовая единица измерения
    """
    @property
    def base(self) -> 'range_model':
        return self.__base
    
    @base.setter
    def base(self, value: 'range_model'):
        validator.validate(value, 'range_model')
        self.__base = value

    @property
    def name(self) -> 'range_model':
        return self.__name
    
    @name.setter
    def base(self, value: 'range_model'):
        validator.validate(value, str)
        self.__name = value 
            
    def __init__(self, value, name, base = None):
        self.__value = None
        self.__base = None
        self.__name = None

        self.value = value
        self.base = base
        self.name = name

