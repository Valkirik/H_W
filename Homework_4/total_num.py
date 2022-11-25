def num(a: int, b: int) -> int:
  while a != b:
    if a >= b:
      a -= b
    else:
      b -= a
  return a

print(num(a=10, b=5))

































