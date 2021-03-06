#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""



import datetime
import sys

from dataproperty import DataPropertyExtractor
from typepy import Typecode


def display_col_dp(dp_list, attr_name):
    """
    show a value assocciated with an attribute for each
    DataProperty instance in the dp_list
    """

    print()
    print("---------- {:s} ----------".format(attr_name))
    print([getattr(dp, attr_name) for dp in dp_list])


def main():
    # sample data definitions
    dt = datetime.datetime(2017, 1, 1, 0, 0, 0)
    inf = float("inf")
    nan = float("nan")
    data_matrix = [
        [1, 1.1,  "aa",   1,   1,     True,   inf,   nan,   dt],
        [2, 2.2,  "bbb",  2.2, 2.2,   False,  "inf", "nan", dt],
        [3, 3.33, "cccc", -3,  "ccc", "true", inf,
            "NAN", "2017-01-01T01:23:45+0900"],
    ]

    # extract property for each column from a matrix
    dp_extractor = DataPropertyExtractor()
    dp_extractor.header_list = [
        "int", "float", "str", "num", "mix", "bool", "inf", "nan", "time"]
    dp_extractor.data_matrix = data_matrix
    col_dp_list = dp_extractor.to_col_dataproperty_list()

    print("---------- typename ----------")
    print([Typecode.get_typename(dp.typecode) for dp in col_dp_list])

    display_col_dp(col_dp_list, "align")
    display_col_dp(col_dp_list, "ascii_char_width")
    display_col_dp(col_dp_list, "decimal_places")

    return 0


if __name__ == "__main__":
    sys.exit(main())
