from saving import save_shape

def triangle(base: int, fill: bool = False, savefile: None | str = None) -> None:
  """
  prints a triangle of width 'base' using '*' characters.

  Arguments:
    - base     : integer, should be uneven
    - fill     : bool, whether to fill the shape
    - savefile : None or str, if a string is given, saves the shape to a
                 file with name `savefile`. If no extension is given, the
                 file will receive the .txt extension.
  
  Returns:
    -
  """

  # raise error if base is even
  if base % 2 == 0:
    raise ValueError(f"Value for base must be uneven and can therefore not be {base}")

  # add base
  layers = [base*"*"]
  whitespace = 1
  base -= 2

  # add edges
  while base > 1:
    if fill:
      layers.append(whitespace*" " + "*"*base + whitespace * " ")
    else:
      layers.append(whitespace*" " + "*" + (base-2)*" " + "*" + whitespace * " ")
    base -= 2
    whitespace += 1
  
  # add top
  layers.append(whitespace*" " + "*" + whitespace*" ")
  
  if savefile is not None:
    save_shape("\n".join(reversed(layers)), savefile)

  print("\n".join(reversed(layers)))

  
def rectangle(width:int, height:int, fill: bool = False, savefile: None | str = None) -> None:

  """
  prints a rectangle of size 'width' x 'height using '*' characters.

  Arguments:
    - width    : integer, should be larger than 0
    - height.  : integer, should be larger than 0
    - fill     : bool, whether to fill the shape
    - savefile : None or str, if a string is given, saves the shape to a
                 file with name `savefile`. If no extension is given, the
                 file will receive the .txt extension.
  
  Returns:
    - 
  """

  if width <= 0:
    raise ValueError(f"width must be larger than 0, {width} <= 0")
  if height <= 0:
    raise ValueError(f"height must be larger than 0, {height} <= 0")

  if fill:
    layers = height*[width*"*"]
  else:
    # add base
    layers = [width*"*"]
    height -= 1
    while height > 1:
      layers.append( "*" + (width > 1) * ((width-2)*" " + "*"))
      height -= 1
    
    layers.append(width*'*')

  if savefile is not None:
    save_shape("\n".join(reversed(layers)), savefile)


  print("\n".join(layers))


def hexagon(edge_length: int = 2) -> None:
  """
  draws a hexagon of with edges of size 'edge_length' using the turtle package

  Arguments:
    - edge_length : integer, should be equal or larger than 0 and and uneven number
  
  Returns:
    - 
  """
  import turtle
  
  if (edge_length <= 0):
    raise ValueError(f"edge length must be larger than 0, {edge_length} <= 0")

  turtle.pendown()
  for _ in range(6):
      turtle.forward(edge_length)
      turtle.left(60)
  turtle.penup()

  print(";) got you there")
