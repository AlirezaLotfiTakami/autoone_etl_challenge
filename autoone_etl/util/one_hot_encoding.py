"""
some utilities that are commonly used by users
"""
import math


def one_hot_encode(value, category_list):
    """
    :param value: a value to be encoded and must be one of the category list items. if not a ValueError will be raised
    :param category_list: category domain for one hot encoding
    :return:  encoded one hot value in integer
    """
    try:
        value_index_in_list = category_list.index(value)
        one_hot_encoded_value = pow(2, value_index_in_list)
        return one_hot_encoded_value
    except ValueError as e:
        raise ValueError("category {} can not be find in  {}".format(value, category_list))


def on_hot_decode(value, category_list):
    """
    :param value: a value to be decoded and must in one hot encoding format in the range of provided category list.
    If not a ValueError will be raised.
    :param category_list: category domain for one hot decoding.
    :return: decoded category in string.
    """
    try:
        category_index = math.log(value, 2)
        one_hot_category = category_list[category_index]
        return one_hot_category
    except IndexError as e:
        raise ValueError("value {} can not be decoded to one of this category {}".format(value, category_list))
