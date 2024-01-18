# input for product a
a = int(input("Enter Quantity For Product A ($20) :") ) # quantity from user
aw = input("if you want to wrap these (Y/N):") # choice to wrap or not
ac =0 # wrap count
if(aw =='Y' or aw == 'y'):
  ac =a # wrap count after yes in input

# inputs for product b
b = int(input("Enter Quantity For Product B ($40) :") )
bw = input("if you want to wrap these (Y/N):")
bc =0
if(bw =='Y' or bw == 'y'):
  bc =b

# input for product c
c = int(input("Enter Quantity For Product C ($50) :") )
cw = input("if you want to wrap these (Y/N):")
cc =0
if(cw =='Y' or cw == 'y'):
  cc =c

#  -------------------- calculation / finding best discount -----------------
cart = 20*a +40*b + 50*c ; # cart total
discount = 0; 
distype ="No_Discount_Aypplicable" # discount type initalize with no discount

if(cart>200):
  discount = 10
  distype= "Flat_10_Discount"

if(((a+b+c) >30) and (a>15 or b>15 or c>15)):
    if(c>15):
        discount = max(discount,(c-15)*50*.5)
    if(b>15):
        discount = max(discount,(b-15)*40*.5)
    if(a>15):
        discount = max(discount,(a-15)*20*.5)
    distype = "Tiered_50_Discount"

if(a>10 or b>10 or c>10):
  if(c>10):
    discount = max(discount,(c*50*.05))
  if(b>10):
    discount = max(discount,(b*40*.05))
  if(a>10):
    discount = max(discount,(a*20*.05))
  distype= "Bulk_5_Discount"

if((a+b+c)>20):
  if(discount<cart*.1):
    discount = cart*.1
    distype= "Bulk_10_Discount"

# ------------- shipping and gift wrap fee -----------------

total_Units = a+b+c
ten_units_packs = total_Units//10
not_ten_packs = total_Units%10
ship_fee = ten_units_packs*5
if(not_ten_packs>0):
  ship_fee+=5
gift_wrp_fee = ac+bc+cc

# ------------Printing statements--------------

print(" ")
print("======================================")
print("               Billing")
print("======================================")
print("Product_Name : Quantity : Total_Amount")
print("Product_A : "+ str(a) + " :  $"+ str(20*a))
print("Product_B : "+ str(b) + " :  $"+ str(40*b))
print("Product_C : "+ str(c) + " :  $"+ str(50*c))
print("-------------------------------------")
print("Subtotal :  $" + str(cart))
print("-------------------------------------")
print("Discount_Name_Applied : " + distype)
print("Discount_Amount :   - $"+ str(discount))
print("-------------------------------------")
print("Shipping_Amount :   $"+ str(ship_fee))
print("Gift_Wrap_Amount :   $"+ str(gift_wrp_fee))
print("======================================")
print("Total_Amount :   $"+ str(cart-discount+ship_fee+gift_wrp_fee))
print("======================================")
