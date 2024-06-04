from color import Color
from response_status import ResponseStatus

import json

# Python Enumeration

if __name__ == "__main__":
  ## Introduction to the Python Enumeration

  print(type(Color.RED))              # <enum "Color">
  print(isinstance(Color.RED, Color)) # True
  print(Color.RED.name)               # RED
  print(Color.RED.value)              # 1

  ## Membership and equality

  if Color.RED in Color:
    print("Yes")

  if Color.RED is Color.BLUE:
    print("red is blue")
  else:
    print("red is not blue")

  if Color.RED == 1:
    print("Color.RED == 1")
  else:
    print("Color.RED != 1")

  ## Enumeration members are hashable

  rgb = {
    Color.RED: "#ff0000",
    Color.GREEN: "#00ff00",
    Color.BLUE: "#0000ff"
  }

  ## Access an enumeration member by name and value

  print(Color["RED"])             # Color.RED
  print(Color(1))                 # Color.RED
  print(Color["RED"] == Color(1)) # True

  ## Iterate enumeration members

  for color in Color:
    print(color)

  print(list(Color))

  ## Enumerations are immutable

  # Color["YELLOW"] = 4 # TypeError: 'EnumMeta' object does not support item assignment

  # Color.RED.value = 100 # AttributeError: <enum 'Enum'> cannot set attribute 'value'

  ## Inherits from an enumeration

  ## Python enumeration example

  response = '''{
      "status": "fulfilled"
  }'''

  data = json.loads(response)
  status = data["status"]
  print(ResponseStatus(status))
