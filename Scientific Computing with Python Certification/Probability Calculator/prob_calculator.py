import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = list() 
    for name in kwargs.keys():
      for i in range(kwargs[name]):
        self.contents.append(name)
    
  def draw(self, numberofballs):
    if numberofballs >= len(self.contents):
      return list(self.contents)
    else: 
      a = self.contents
      mylist = []
      for i in range(numberofballs):    
        random_item_from_list = random.choice(a)
        mylist.append(random_item_from_list)
        a.remove(random_item_from_list)
      
      return mylist


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  a = 0
  for k in range(num_experiments):
    check = True
    myhat = copy.deepcopy(hat)
    b = myhat.draw(num_balls_drawn)
    #print(b)
    #print(expected_balls)
    for name in expected_balls.keys():
      if expected_balls[name] > b.count(name):
        #print(name, b.count(name))
        check = False
        break
  

    if check:
      a = a + 1

    #print (a)
  return float(a)/num_experiments

