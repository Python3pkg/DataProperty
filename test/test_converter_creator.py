# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import

import pytest

from dataproperty.converter._core import IntegerConverter
from dataproperty.converter._core import FloatConverter
from dataproperty.converter._core import DateTimeConverter
from dataproperty.converter import IntegerConverterCreator
from dataproperty.converter import FloatConverterCreator
from dataproperty.converter import DateTimeConverterCreator


class Test_ConverterCreator(object):

    @pytest.mark.parametrize(["value", "expected"], [
        [IntegerConverterCreator, IntegerConverter],
        [FloatConverterCreator, FloatConverter],
        [DateTimeConverterCreator, DateTimeConverter],
    ])
    def test_normal(self, value, expected):
        creator = value()
        type_checker = creator.create(None)
        assert isinstance(type_checker, expected)
