# SQL Validators
def check_for_extra_semicolon(SQLStr):
    try:
        if SQLStr.find(';') != -1:
            raise Exception("Extra Semi-Colon Detected!")
    except Exception as e:
        raise e

def check_for_or(SQLStr):
    try:
        if SQLStr.find('or') != -1:
            raise Exception("OR Detected!")
    except Exception as e:
        raise e