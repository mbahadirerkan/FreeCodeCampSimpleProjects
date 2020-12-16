"""
github: mbahadirerkan
arithmetic_arranger: Simple python program to 
printing computations in a format. 
You can reach the project instructions from 
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
"""

def arithmetic_arranger(problems, show = False):
  lengthproblems = len(problems)

  if lengthproblems > 5:
    return "Error: Too many problems."


  result = ""

  #getting data from problems;

  mylist = [a.split() for a in problems]
  
  #in order to print in a format
  widths = list()
  check = False

  for item in mylist:
    if item[1] != '-' and item[1] != '+':
      result = "Error: Operator must be '+' or '-'." 
      break
    elif not item[0].isnumeric() or not item[2].isnumeric():
      result = "Error: Numbers must only contain digits."
      break
    elif len(item[0]) > 4 or len(item[2]) > 4:
      result = "Error: Numbers cannot be more than four digits."
      break
    else:
      width = 0
      for a in item:
        if a.isnumeric() :
          width = max(width, len(a))
          a = int(a)
        
      widths.append(width)
      check = True    

  if check:
    for count in range(4):
      for item in range(len(mylist)):
        
        if count != 1:
          if count == 2:
            result = result + mylist[item][1] + mylist[item][count].rjust(widths[item]  + 1)
            if item != len(mylist) - 1:
              result = result + "".ljust(4)
          elif count == 3:
            for a in range(widths[item] + 2):
              result = result + "-"
            result = result
            if item != len(mylist) - 1:
              result = result + "".ljust(4)
          else:
            result = result + mylist[item][count].rjust(widths[item]  + 2)
            if item != len(mylist) - 1:
              result = result + "".ljust(4)
      if count != 1 and count != 3:
        result = result + "\n"
  
  if show:
    result = result + "\n"
    for item in range(len(mylist)):
      if ord(mylist[item][1]) == 43:
        a = int(mylist[item][2]) + int(mylist[item][0])
      else:
        a = int(mylist[item][0]) - int(mylist[item][2])

      a = str(a)
      result = result + a.rjust(widths[item] + 2)
      if item != len(mylist) - 1:
          result = result + "".ljust(4)

  return result