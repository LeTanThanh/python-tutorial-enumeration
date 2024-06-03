from color import Color

# Python Enumeration

if __name__ == "__main__":
  ## Introduction to the Python Enumeration

  print(type(Color.RED))              # <enum "Color">
  print(isinstance(Color.RED, Color)) # True
  print(Color.RED.name)               # RED
  print(Color.RED.value)              # 1
