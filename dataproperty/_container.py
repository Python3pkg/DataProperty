# encoding: utf-8

'''
@author: Tsuyoshi Hombashi
'''


class MinMaxContainer(object):

    @property
    def min_value(self):
        return self.__min_value

    @property
    def max_value(self):
        return self.__max_value

    def __init__(self, value_list=[]):
        self.__min_value = None
        self.__max_value = None

        for value in value_list:
            self.update(value)

    def diff(self):
        try:
            return self.max_value - self.min_value
        except TypeError:
            return float("nan")

    def mean(self):
        try:
            return (self.max_value + self.min_value) * 0.5
        except TypeError:
            return float("nan")

    def update(self, value):
        if value is None:
            return

        if self.__min_value is None:
            self.__min_value = value
        else:
            self.__min_value = min(self.__min_value, value)

        if self.__max_value is None:
            self.__max_value = value
        else:
            self.__max_value = max(self.__max_value, value)
