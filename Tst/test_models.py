                                                                        
import unittest
from Src.Models.range import range_model
from Src.Models.nomenclature import nomenclature_model

"""
Набор тестов для проверки работы моделей
"""
class test_models(unittest.TestCase):

    """
    Проверить вариант сравнения (по коду)
    """
    def test_nomenclature_model(self):
        # Подготовка
        item1 = nomenclature_model()
        item1.name = "test1"

        item2 = nomenclature_model()
        item2.name = "test1"

        # Проверка
        assert item1 != item2


    """
    Проверить вариант сравнения (по наименованию)
    """
    def test_range_model(self):
        # Подготовка
        item1 = range_model()
        item1.name = "test1"

        item2 = range_model()
        item2.name = "test1"

        # Проверка
        assert item1 == item2
    def test_nomenclature_exists(self):
        # Проверяем, что данные по номенклатуре созданы
        assert len(self.__reposity.data['nomenclatures']) > 0

    def test_ranges_exists(self):
        # Проверяем, что данные по единицам измерения созданы
        assert len(self.__reposity.data['ranges']) > 0

    def test_groups_exists(self):
        # Проверяем, что данные по группам созданы
        assert len(self.__reposity.data['group']) > 0

    def test_recipes_exists(self):
        # Проверяем, что данные по рецептам созданы
        assert len(self.__reposity.data['recipes']) > 0


    