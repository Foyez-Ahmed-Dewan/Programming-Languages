#example -- learn a new thing
# in c++, we can't define a function inside a function, but in python we can do it
def outer_f (a, b):
  def inner_f (c, d):
    return c + d
  return inner_f(a, b)

print (outer_f (5, 10)) #output: 15

