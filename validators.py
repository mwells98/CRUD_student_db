import re

def valid_id(id):
    return re.fullmatch(r'\d{1,8}', str(id))

def valid_name(name):
    return re.fullmatch(r'[A-Za-z]{1,12}', name)

def valid_grade(grade):
    return re.fullmatch(r'[ABCDF]', grade.upper())

def valid_email(email):
    return re.fullmatch(r'[^@]+@[^@]+\.com', email)
