def save_shape(shape: str, filename: str) -> None:

  # check if file has extension
  if len(filename.split(".")) == 1:

    # add txt extension
    filename = filename + ".txt"

  with open(filename, "w+") as f:
    f.write(shape)

