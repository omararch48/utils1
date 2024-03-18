from typing import Any, List, Dict


def identity(value: Any, *args: Any, **kwargs: Any) -> Any:
    """Return the same value passed as input.

    :param value: The input value.
    :return: The same value passed as input.
    """
    return value


def replace_code(value_code: str, *args: Any, **kwargs: Any) -> str:
    """Replace a code with its corresponding value.

    :param value_code: The code to be replaced.
    :return: The corresponding value for the code, if found; otherwise, None.
    """
    innder_code_dictionary = {
        'c-23': 'Denuncia',
        'c-24': 'Fraude',
        'c-25': 'Acoso',
    }
    return innder_code_dictionary.get(value_code)


def sum_days(
        items_list: List[Dict[str, Any]], *args: Any, **kwargs: Any
    ) -> str:
    """Calculate the sum of 'value' fields in a list of dictionaries.

    :param items_list: A list of dictionaries containing 'value' fields.
    :param args: Additional arguments. The first argument is used as a prefix in the return string.
    :return: A string representing the sum of 'value' fields with the provided prefix.
    """
    sum = 0
    for element in items_list:
        sum += element['value']
    return f'{args[0]}{sum}'


def get_day(datetima_str: str, *args: Any, **kwargs: Any) -> str:
    """Extract the day from a datetime string and replace '/' with a special character.

    :param datetima_str: The datetime string from which to extract the day.
    :param args: Additional arguments (not used in this function).
    :param kwargs: Additional keyword arguments. 'special_char' is used to specify the character to replace '/'.
    :return: The extracted day with '/' replaced by the specified special character.
    """
    day, _ = datetima_str.split()
    special_char = kwargs['special_char']
    return day.replace('/', special_char)


CALLBACKS = {
    'created_at': get_day,
    'history': identity,
    'type': replace_code,
}