from pprint import pprint
class Order:
  def __init__(self, date, isPrepaid, number, price):
    self.date = date
    self.isPrepaid = isPrepaid
    self.number = number
    self.price = price

  def dispatch(self):
    print('\nDispatched Order ' + str(self.number) + ' with date ' + str(self.date))

  def close(self):
    print('\nClosed Order ' + str(self.number) + ' with date ' + str(self.date))

class OrderLine:
  def __init__(self, product, quantity, price):
    self.product = product
    self.quantity = quantity
    self.price = price

class Customer:
  def __init__(self, name, address, creditRating):
    self.name = name
    self.address = address
    self.creditRating = creditRating


class CorporateCustomer(Customer):
  def __init__(self, target, creditLimit):
    super().__init__(target.name, target.address, target.creditRating)
    self.creditLimit = creditLimit

  def remind(self):
    print('\nReminder from ' + str(self.name))

class PersonalCustomer(Customer):
  def __init__(self, target, creditCardID):
    super().__init__(target.name, target.address, target.creditRating)
    self.creditCardID = creditCardID
  
def main():
  print("\nCreate Order 1:")
  order1 = Order("3 Januari", False, 1, 34000)
  pprint(vars(order1))

  order1.dispatch()
  order1.close()

  print("\nCreate Order Line 1:")
  orderline1 = OrderLine("Laptop Geming", 1, 30000000)
  pprint(vars(orderline1))

  fatih = Customer("M Fatih", "Jl. Parjaka", "A")
  milla = Customer("N Milla", "Jl. Hepi", "A-")

  print("\nCustomer List:\n")

  pprint(vars(fatih))
  pprint(vars(milla))

  print("\nCustomer Added to Personal:")
  cardMilla = PersonalCustomer(milla, "909980")
  pprint(vars(cardMilla))

  print("\nCustomer Added to Corporate:")
  corpFatih = CorporateCustomer(fatih, 800000)
  pprint(vars(corpFatih))

  corpFatih.remind()
  return

if __name__ == "__main__":
  main()
