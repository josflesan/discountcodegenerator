###################################################################################
#                       H   E   A   D   E   R
#
# DiscountCodeGenerator  Copyright (C) 2019  Lemur
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it
# under certain conditions.
#
###################################################################################
CODE_DELIMITER = "-"
FILE_DELIMITER = "/"


def generate_code():
    code = ""

    discount_value = int(input("Input discount value: "))
    if (discount_value > 0) and (discount_value < 100):
        code += str(discount_value) + CODE_DELIMITER
    else:
        return 13  # Error Code 13: The data is invalid.

    code_id = f_codeID(seed)
    code += str(code_id) + CODE_DELIMITER

    today_date += f_today()
    code += today_date + CODE_DELIMITER

    expiration_days = int(input("Input expiration days: "))
    if expiration_days > 0:
        code += str(expiration_days) + CODE_DELIMITER
    else:
        return 13  # Error Code 13: The data is invalid.

    valid_flag = f_validate(code)
    code += valid_flag

    return code


def f_today():
    import datetime
    now = datetime.datetime.now()
    today = str(now.day) + str(now.month) + str(now.year)

    return today

