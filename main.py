import math



def find_roots(a, b, c):
  discriminant = b**2 - 4 * a * c

  if discriminant < 0:
    return None, None
  elif discriminant == 0:
    x = -b / (2 * a)
    return x, x
  else:
    x1 = (-b - math.sqrt(discriminant)) / (2 * a)
    x2 = (-b + math.sqrt(discriminant)) / (2 * a)
    return x1, x2