import math

class Rectangle:
  
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2*self.width) + (2*self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return 'Too big for picture.'
    else:  
      return ('*' * self.width + '\n') * self.height

  def get_amount_inside(self,shape):

    if shape.width > self.width or shape.height > self.height:
      return 0

    else:
      height_ratio = self.height / shape.height
      width_ratio = self.width / shape.width

      if height_ratio.is_integer() and width_ratio.is_integer():
        return height_ratio * width_ratio
      
      elif height_ratio.is_integer() and not width_ratio.is_integer():
        return height_ratio

      elif not height_ratio.is_integer() and width_ratio.is_integer():
        return width_ratio

      elif not height_ratio.is_integer() and not width_ratio.is_integer():
        return math.floor(min(height_ratio,width_ratio))

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
  
  def __init__(self,side):
    self.width = self.height = side

  def set_side(self,side):
    self.width = self.height = side

  def set_width(self,width):
    self.width = self.height = width

  def set_height(self,height):
    self.width = self.height = height 

  def __str__(self):
    return f'Square(side={self.width})'    