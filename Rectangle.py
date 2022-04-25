class Rectangle:
  def __init__(self,x,y,h,w):
    '''
    Defines the instance variables for a rectangle object
    Args: self-object
          x-x coordinate of the upper left hand corner (int)
          y-y coordinate of the upper left hand corner (int)
          h-height of rectangle(int)
          w-width of rectangle(int)
    Return: None
    '''
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    if self.x<0:
      self.x=0
    if self.y<0:
      self.y=0
    if self.height<0:
      self.height=0
    if self.width<0:
      self.width=0
    
  def __str__(self):
    '''
    Returns the coordinates and size of the rectangle
    Args: self-object
    Return: rectangle statistics
    '''
    return "x: "+str(self.x)+",y: "+str(self.y)+",height: "+str(self.height)+",width: "+str(self.width)
    