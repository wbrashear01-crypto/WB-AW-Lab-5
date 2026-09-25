def ugly_number(n):
  """
  ## add more to the docstring, including additional tests
  
  >>> ugly_number(6)
  True
  >>> ugly_numer(1)
  True
  >>> ugly_number(14)
  False
  """
def ugly_number(n):
    while n%3==0 or n%2==0 or n%5==0:
        if n%3==0:
            n=n/3
        elif n%5==0:
            n=n/5
        elif n%2==0:
            n=n/2
    if n==1:
        return True
    elif n!= 1:
        return False
