amount = 0
net_unit = float(input("Enter any unit value: "))
if(net_unit <= 100):
  amount = 0
  print("no Change", amount)
elif(net_unit > 100 and net_unit <= 200):
  amount = (net_unit - 100) * 5
  print("RS 5", amount)
elif(net_unit>200):
  amount = ((net_unit - 200)*10)+500
  print("RS 10",amount)


  #fail or pass:
marks = float(input("Enter yours marks: "))
if (marks > 90):
  print("you Got A", marks)
elif(marks >80 and marks <= 90):
  print("You Got B", marks)
elif(marks >=60 and marks<= 80):
  print("You Got C", marks)
elif(marks >=33 and marks <60):
  print("You Got D", marks)
else:
  print("you will Fail")

#slary
tax = 0
cost = int(input("Enter the cost price: "))
if(cost >100000):
  tax = (15/100)*cost
  print("tax to paid1", tax)
elif(cost >50000 and cost<= 100000):
  tax = (10/100)*cost
  print("tax to paid2", tax)
elif(cost <=50000):
  tax = (5/100)*cost
  print("tax to paid3", tax)

else:
  print("tax didn't paid")

#Weekend
number = int(input("Enter the number 1 to 7: "))

if(number==1):
  print("Satarday")
elif(number==2):
  print("Sunday")
elif(number==3):
  print("Monday")
elif(number==4):
  print("Thursday")
elif(number==5):
  print("Whensday")
elif(number==6):
  print("Thusday")
elif(number==7):
  print("Friday")

