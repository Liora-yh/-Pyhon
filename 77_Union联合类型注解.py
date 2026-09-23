from typing import Union

my_list: list[Union[str, int]] = [1, 2, "Liora", "Luoyuhua"]

my_dict: dict[str, Union[str, int]] = {"name": "落雨花", "age": 21}

def func(data: Union[int, str]) -> Union[int, str]:
    pass