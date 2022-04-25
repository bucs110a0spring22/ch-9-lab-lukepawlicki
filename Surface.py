from Rectangle import Rectangle

class Surface:
  def __init__(self,filename,x,y,h,w):
    '''
    Uses rectangle class to create a surface
    Args: self-object
          filename-saves an image (str)
          x-x coordinate of the upper left hand corner (int)
          y-y coordinate of the upper left hand corner (int)
          h-height of rectangle(int)
          w-width of rectangle(int)
    Return: None
    '''
    self.image = filename
    self.rect = Rectangle(x,y,h,w)

  def getRect(self): 
    '''
    Returns the rectangle object
    Args: self-object
    Return: the rectangle object
    '''
    return self.rect 
    