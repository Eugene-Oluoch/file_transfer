def is_map_empty(map):
    len_of_map = len(list(map.keys()))
    return len_of_map == 0

def get_error_key(map):
    errors_keys = list(map.keys())
    return errors_keys[0]