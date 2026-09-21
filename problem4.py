def power_of_three(n):
  """
  ### add to the docstring, including doctests

  >>> power_of_three(27)
  True
  >>> power_of_three(0)
  False
  >>> power_of_three(-10)
  False
  >>> power_of_three(9)
  True
  """
  if n<1:
    return False
  while n%3==0:
    n=n//3
  return n==1
