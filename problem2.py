def bologna_latin(string):
  """
  ### add to the docstring, including additional doctests
  
  >>> bologna_latin("programming")
  "rogrammingpay"
  >>> bologna_latin("hello world")
  "ello worldhay"
  >>> bologna_latin("a")
  "aay"
  >>> bologna_latin("september")
  "emptembersay"
  """
  return string[1:] + string[0] + "ay"
