from Src.Core.abstract_logic import abstract_logic
from Src.data_reposity import data_reposity
from Src.Core.validator import validator
from Src.Models.group import group_model
from Src.settings_manager import settings_manager
from Src.settings import settings
from Src.Models.nomenclature import nomenclature_model
from Src.Models.range import range_model
from Src.Models.recipe import recipe_model
from Src.Models.ingredients import Ingredient
import datetime


"""
Сервис для реализации первого старта приложения
"""
class start_service(abstract_logic):
    __reposity: data_reposity = None
    __settings_manager: settings_manager = None

    def __init__(self, reposity: data_reposity, manager: settings_manager ) -> None:
        super().__init__()
        validator.validate(reposity, data_reposity)
        validator.validate(manager, settings_manager)
        self.__reposity = reposity
        self.__settings_manager = manager

    """
    Текущие настройки
    """
    @property 
    def settings(self) -> settings:
        return self.__settings_manager.settings

    """
    Сформировать группы номенклатуры
    """
    def __create_nomenclature_groups(self):
        list = []
        list.append(group_model.default_group_cold())
        list.append( group_model.default_group_source())
        self.__reposity.data[data_reposity.group_key()] = list    

    """
    Первый старт
    """
    def create(self):
        # Создание групп номенклатуры
        self.__create_nomenclature_groups()
        
        # Создание единиц измерения
        self.__create_ranges()
        
        # Создание номенклатуры
        self.__create_nomenclatures()

        # Формирование рецептов
        self.create_receipts()

    """
    Перегрузка абстрактного метода
    """
    def set_exception(self, ex: Exception):
        self._inner_set_exception(ex)    
    
    def __create_ranges(self):
        range1 = range_model(1, "граммы")

        range2 = range_model(1, "шт")

        self.__reposity.data['ranges'] = [range1, range2]

    def __create_nomenclatures(self):
        nomenclature1 = nomenclature_model()
        nomenclature1.name = "Пшеничная мука"
        nomenclature1.group = group_model.default_group_source()
        nomenclature1.range = self.__reposity.data["ranges"][0]

        nomenclature2 = nomenclature_model()
        nomenclature2.name = "Сахар"
        nomenclature2.group = group_model.default_group_source()
        nomenclature2.range = self.__reposity.data["ranges"][0]

        nomenclature3 = nomenclature_model()
        nomenclature3.name = "Сливочное масло"
        nomenclature3.group = group_model.default_group_source()
        nomenclature3.range = self.__reposity.data["ranges"][0]

        nomenclature4 = nomenclature_model()
        nomenclature4.name = "Яйца"
        nomenclature4.group = group_model.default_group_source()
        nomenclature4.range = self.__reposity.data["ranges"][1]
        
        nomenclature5 = nomenclature_model()
        nomenclature5.name = "Ванилин"
        nomenclature5.group = group_model.default_group_source()
        nomenclature5.range = self.__reposity.data["ranges"][0]

        nomenclature6 = nomenclature_model()
        nomenclature6.name = "Шоколад"
        nomenclature6.group = group_model.default_group_source()
        nomenclature6.range = self.__reposity.data["ranges"][0]

        self.__reposity.data['nomenclatures'] = [nomenclature1, nomenclature2, nomenclature3, nomenclature4, nomenclature5, nomenclature6]

    def create_receipts(self):

        reciep1_ingredients = [
            Ingredient(self.__reposity.data['nomenclatures'][0], range_model(150, "граммы")),
            Ingredient(self.__reposity.data['nomenclatures'][1], range_model(50, "граммы")),
            Ingredient(self.__reposity.data['nomenclatures'][5], range_model(100, "граммы")),
            Ingredient(self.__reposity.data['nomenclatures'][3], range_model(2, "шт")),
            Ingredient(self.__reposity.data['nomenclatures'][2], range_model(50, "граммы")),
        ]

        reciep1_coocking_steps = [
                "Подготовьте ингредиенты",
                "Растопите шоколад с маслом",
                "Взбейте яйца с сахаром, добавьте муку",
                "Растопите шоколад с маслом"
        ]
        recipe1 = recipe_model(
            "Вафли с шоколадом",
            datetime.timedelta(minutes=25),
            reciep1_ingredients,
            reciep1_coocking_steps
        )

        recipe2_ingredients = [
            Ingredient(self.__reposity.data['nomenclatures'][0], range_model(100, "граммы")),  # Пшеничная мука
            Ingredient(self.__reposity.data['nomenclatures'][1], range_model(80, "граммы")),   # Сахар
            Ingredient(self.__reposity.data['nomenclatures'][2], range_model(70, "граммы")),   # Сливочное масло
            Ingredient(self.__reposity.data['nomenclatures'][3], range_model(1, "шт")),        # Яйца
            Ingredient(self.__reposity.data['nomenclatures'][4], range_model(5, "граммы")),    # Ванилин
        ]

        recipe2_cooking_steps = [
            "Подготовьте необходимые продукты. Из данного количества у меня получилось 8 штук диаметром около 10 см.",
            "Масло положите в сотейник с толстым дном. Растопите его на маленьком огне на плите, на водяной бане либо в микроволновке.",
            "Добавьте в теплое масло сахар. Перемешайте венчиком до полного растворения сахара. От тепла сахар довольно быстро растает.",
            "Добавьте в масло яйцо. Проверьте, чтобы масло не было слишком горячим, иначе яйцо может свариться. Перемешайте до однородности.",
            "Всыпьте муку, добавьте ванилин и перемешайте массу венчиком до состояния гладкого однородного теста.",
            "Разогрейте вафельницу по инструкции. Смазывать вафельницу маслом необязательно, так как в тесте достаточно жира.",
            "Выложите тесто по столовой ложке. Пеките несколько минут до золотистого цвета.",
            "Снимите вафлю лопаткой. Горячая вафля очень мягкая, как блинчик.",
        ]

        recipe2 = recipe_model(
            "ВАФЛИ ХРУСТЯЩИЕ В ВАФЕЛЬНИЦЕ",
            datetime.timedelta(minutes=20),
            recipe2_ingredients,
            recipe2_cooking_steps
        )
        self.__reposity.data['recipes'] = [recipe1, recipe2]
