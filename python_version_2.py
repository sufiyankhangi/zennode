class ShoppingCenter():
  def __init__(self,quan_a, flag_a, quan_b, flag_b, quan_c, flag_c):
    self.quan_a = quan_a
    self.flag_a = flag_a
    self.quan_b = quan_b
    self.flag_b = flag_b
    self.quan_c = quan_c
    self.flag_c = flag_c
    # self.current_price = None
    # self.gift_wrap_fee = None
    # self.shipping_fee = None
    # self.max_disc = None
    # self.category = None
  
  def calculate(self):
    self.a,self.b, self.c = 0,0,0
    if quan_a > 0:
      self.a = quan_a*20
    if quan_b>0:
      self.b = quan_b*40
    if quan_c>0:
      self.c = quan_c*50

    self.current_price = self.a + self.b + self.c
    self.max_disc = 0
    self.category = ""
    q = self.quan_a + self.quan_b + self.quan_c

    if self.current_price > 200: #1st catgeory
      disc = 10
      if disc > self.max_disc:
        self.max_disc = disc
      self.category = 1

    if self.quan_a>10 or self.quan_b >10 or self.quan_c>10: #2nd category
      disc = 0
      if self.quan_a>10:
        disc += self.quan_a*20*0.05
      if self.quan_b>10:
        disc += self.quan_b*40*0.05
      if self.quan_c>10:
        disc += self.quan_c*50*0.05
      if disc > self.max_disc:
        self.max_disc = disc
        self.category = 2

    if q > 20: #3rd
      disc = self.current_price*0.1
      if disc > self.max_disc:
        self.max_disc = disc
        self.category = 3

    if q > 30: #4th 
      if self.quan_a > 15:
        disc = (self.quan_a-15)*20*0.5
      if self.quan_b > 15:
        disc = (self.quan_b-15)*40*0.5
      if self.quan_c > 15:
        disc = (self.quan_c-15)*50*0.5
      
      if disc > self.max_disc:
        self.max_disc = disc
        self.category = 4
    
    self.gift_wrap_fee, self.shipping_fee= 0,0
    if flag_a == 1:
      self.gift_wrap_fee += quan_a
    if flag_b == 1:
      self.gift_wrap_fee += quan_b
    if flag_c == 1:
      self.gift_wrap_fee += quan_c
    if q>0:
      quo = q//10
      rem = q%10
      if rem>0:
        self.shipping_fee = (q//10+1)*5
      else:
        self.shipping_fee = (q//10)*5
    self.result = [self.quan_a, self.a, self.quan_b, self.b, self.quan_c, self.c, self.current_price, self.gift_wrap_fee, self.shipping_fee, self.max_disc, self.category]
    self.print_data()

  def print_data(self):
    if self.quan_a>0:
      print("Product Category of A : Total Price -> {}$, Net Quantity -> {}.".format(self.a,  self.quan_a))
    if self.quan_b>0:
      print("Product Category of B : Total Price -> {}$, Net Quantity -> {}.".format(self.b, self.quan_b))
    if self.quan_c>0:
      print("Product Category of C : Total Price -> {}$, Net Quantity -> {}.".format(self.c, self.quan_c))

    print()
    print("SubTotal -> {}$".format(self.current_price))

    print()
    if self.category == 0:
      print("No Discount Applicaple")
    else:
      if self.category == 1:
        print("Discount Category 1 Applicable -> {}".format("flat_10_discount"))
      elif self.category == 2:
        print("Discount Category 2 Applicable -> {}".format("bulk_5_discount"))
      elif self.category == 3:
        print("Discount Category 3 Applicable -> {}".format("bulk_10_discount"))
      elif self.category == 4:
        print("Discount Category 4 Applicable -> {}".format("tiered_50_discount"))
      print("Total Discount applicable for the above Category is -> {}$".format(self.max_disc))

    print()
    if self.gift_wrap_fee>0:
      print("Gift Wrap Fee -> {}$, Shipping Fee -> {}$".format(self.gift_wrap_fee, self.shipping_fee))
    else:
      print("Shipping Fee -> {}$".format(self.shipping_fee))
    print()

    print("Total Price - > {}$".format(self.current_price + self.gift_wrap_fee + self.shipping_fee - self.max_disc))
1
print("Enter Quantity for the Product A ->" , end = " ")    
quan_a = int(input())
print("Do you want to add as gift, Type y or n for  Product A ->" , end = " ")
flag = input()
if flag == "y": flag_a = 1
else: flag_a = 0
print()
print("Enter Quantity for the Product B ->" , end = " ")    
quan_b = int(input())
print("Do you want to add as gift, Type y or n for  Product B ->" , end = " ")
flag = input()
if flag == "y": flag_b = 1
else: flag_b = 0
print()
print("Enter Quantity for the Product C ->" , end = " ")    
quan_c = int(input())
print("Do you want to add as gift, Type y or n for  Product C ->" , end = " ")
flag = input()
if flag == "y": flag_c = 1
else: flag_c = 0
print()

shopping_center = ShoppingCenter(quan_a,flag_a, quan_b, flag_b, quan_c, flag_c)
shopping_center.calculate()
