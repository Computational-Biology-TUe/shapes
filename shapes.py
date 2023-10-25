def triangle(base: int, fill: bool = False) -> None:
  """
  prints a triangle of width 'base' using '*' characters.

  Arguments:
    - base : integer, should be uneven
    - fill : bool, whether to fill the shape
  
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
  
  print("\n".join(reversed(layers)))

def rectangle(width:int, height:int) -> None:
  """
  prints a rectangle of size 'width' x 'height using '*' characters.

  Arguments:
    - width  : integer, should be larger than 0
    - height : integer, should be larger than 0
  
  Returns:
    - 
  """

  if width <= 0:
    raise ValueError(f"width must be larger than 0, {width} <= 0")
  if height <= 0:
    raise ValueError(f"height must be larger than 0, {height} <= 0")


  # add base
  layers = [width*"*"]
  height -= 1
  while height > 1:
    layers.append( "*" + (width > 1) * ((width-2)*" " + "*"))
    height -= 1
  
  layers.append(width*'*')

  print("\n".join(layers))

triangle(7, False)