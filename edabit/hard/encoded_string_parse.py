"""
parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}
Notes
The string will always be in the same format: first name, last name and id with zeros between them.
id numbers will not contain any zeros.
Bonus: Try solving this using RegEx.
"""

def parse_code(string):
    split_string = string.split("0")
    arr = []
    for item in split_string:
        if item != "":
            arr.append(item)
    ret = {
        "first_name": arr[0],
        "last_name": arr[1],
        "id": arr[2]
    }
    return ret

print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))
