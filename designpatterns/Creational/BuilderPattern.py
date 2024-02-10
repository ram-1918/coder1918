"""
Builder pattern is a creational pattern, 
it is useful to create an object with lots of possible configuration options
"""
from abc import ABC, abstractmethod
from typing import Any


class MealBuilderInterface(ABC):
    @abstractmethod
    def build_burger(self):
        raise NotImplementedError

    @abstractmethod
    def build_drink(self):
        raise NotImplementedError

    @abstractmethod
    def build_side(self):
        raise NotImplementedError


class VegitarianMealPlan(MealBuilderInterface):
    def __init__(self):
        self.meal = []

    def build_burger(self):
        self.meal.append('Burger')
        return self

    def build_drink(self):
        self.meal.append('Drink')
        return self

    def build_side(self):
        self.meal.append('Side')
        return self


class Chef:
    # def __new__(): print('Chef X is now online')

    def __init__(self, mealObj):
        self.name = mealObj.name

    # def constuct_veg_meal(self):
    #     print(self.__class__)
    #     self.obj.build_burger()
    #     self.obj.build_drink()
    #     self.obj.build_side()
    #     return self.obj.meal


if __name__ == '__main__':
    vegPlanObj = VegitarianMealPlan()
    vegPlanObj.build_burger().build_drink().build_drink()
    print(vegPlanObj.meal)
