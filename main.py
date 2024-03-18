from typing import Any, Dict, List, Tuple, Callable, Optional


def search_in_dictionary(
        dictionary: Dict[str, Any] = {}, key: str = ''
    ) -> Optional[Any]:
    """Search for a key in a nested dictionary and return its value.

    :param dictionary: The dictionary to search in. Default is an empty dictionary.
    :param key: The key to search for.
    :return: The value corresponding to the key if found, otherwise None.
    """
    if not dictionary:
        return None
    aux_value = None
    if key not in dictionary:
        for _, dict_value in dictionary.items():
            if isinstance(dict_value, dict):
                aux_value = search_in_dictionary(dict_value, key)
                if aux_value:
                    break
    if aux_value:
        return aux_value
    value = dictionary.get(key)
    return value


def build_new_value(
        raw_value: Any,
        callback: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
) -> Tuple[str, Any]:
    """Build a new value by applying a callback function to the raw value.

    :param raw_value: The raw value to be processed.
    :param callback: The callback function to apply to the raw value.
    :param args: Additional positional arguments to pass to the callback.
    :param kwargs: Additional keyword arguments to pass to the callback.
    :return: A tuple containing a string indicating the status and the processed value.
    """
    new_value: Any = None
    try:
        new_value = callback(raw_value, *args, **kwargs)
    except:
        new_value = ''
    return new_value


if __name__ == '__main__':

    from RAW_DATA import RAW_DATA
    from KEYSCOLUMNS import KEYSCCOLUMNS
    from CALLBACKS import CALLBACKS

    data: Optional[List[Dict[str, Any]]] = []

    for dictionary in RAW_DATA:
        new_dictionary = {}
        for key, _ in KEYSCCOLUMNS:
            if key == 'created_at':
                new_dictionary[key] = build_new_value(
                    search_in_dictionary(dictionary, key),
                    CALLBACKS[key],
                    special_char = '-',
                )
            elif key == 'history': 
                new_dictionary[key] = build_new_value(
                    search_in_dictionary(dictionary, key),
                    CALLBACKS[key],
                    'La suma total es: ',
                )
            else:
                new_dictionary[key] = build_new_value(
                    search_in_dictionary(dictionary, key),
                    CALLBACKS[key],
                )
        data.append(new_dictionary)




    for element in data:
        print('\n')
        for key, value in element.items():
            print(f'\t{key}: {value}')