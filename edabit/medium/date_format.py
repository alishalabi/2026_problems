"""
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

Examples
format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"
"""

def format_date(date):
    array = date.split("/")
    ret = array[2] + array[1] + array[0]
    return ret

print(format_date("11/12/2019"))
print(format_date("12/31/2019"))
print(format_date("01/15/2019"))
