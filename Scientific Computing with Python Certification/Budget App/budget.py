class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()
    self.spent = 0

  def deposit(self, amount, description = ""):
    #description = str(description)
    self.ledger.append({"description": description, "amount": amount})

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      description = str(description)
      self.ledger.append({"description": description, "amount": -amount})
      self.spent += amount
      return True
    else:
      return False

  def get_balance(self):
    result = 0
    for value in self.ledger:
      result = result + value["amount"]
    return result 

  def transfer(self, amount, Category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {Category.name}")
      Category.deposit(amount, f"Transfer from {self.name}")
      self.spent += amount
      return True
    else:
      return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __repr__(self):
    result = ""
    result += self.name.center(30 ,"*") + "\n"
    for item in self.ledger:
      key = str(item["description"])
      if len(key) > 23:
        key = key[:23]
      
      value = str(format(item["amount"], ".2f"))
      if len(value) > 7:
        value = value[:7]
      
      result = result + str(key).ljust(23) + str(value).rjust(7) + "\n" 
    
    result = result + f"Total: {self.get_balance()}"
    
    return result 


def create_spend_chart(categories):
  result = ""
  result = result + "Percentage spent by category\n"

  total = 0
  count = 0


  for category in categories:
    count = count + 1 
    total = total + category.spent


  for line in reversed(range(11)):
    result = result + f"{line * 10}|".rjust(4)
    for category in categories: 
      if round(category.spent * 10 / total, 2) >= (line): 
        result = result + " o ".rjust(3)
      else: 
        result = result + "   ".rjust(3)

    result = result + " \n"

  adding = ""
  for i in range(count):
    adding = adding + "---"
  result = result + "".rjust(4) + adding + "-" + "\n"
 
  length = 0
  for category in categories:
    if len(category.name) > length:
      length = len(category.name)

  for line in range(length):
    result = result + "".rjust(4)
    for category in categories:
      if len(category.name) > line:
        result = result + " " + (category.name[line]) + " "
      else:
        result = result + "   "
    
    

    if line != length - 1:
      result = result + " \n"
    else:
      result = result + " "


  return result 