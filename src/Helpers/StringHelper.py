def check_string_in_list(target_string, string_list):
    for string in string_list:
        if string == target_string:
            return True
    return False