a = int (input(" Please Enter the First Number: ")) 

b = int (input(" Please Enter the second number: "))

c = int (input(" Please Enter the third number: "))

average=(a+b+c)/3

print("The average of three numbers is ", average)



a= 25
b= int('25')
c=25
sum = a+b+c
h=str(sum)
print ("sum is ", h)



from math import *
# create a for loop
for i in range(0, 360, 15):
    # then print the sine and cosine of the angles
    print(i, '---', round(sin(i), 4), round(cos(i),4))


    gross_income = int (input ("enter your gross income to nearest penny."))
standard_deduction= 10000
dependent_deduction= 3000
Tax_rate=20%gross_income
No_of_dependents = int(input ("No of dependents:"))
Taxable_income=gross_income -standard_deduction-(dependent_deduction*No_of_dependents)
tax=Taxable_income * 20%gross_income
print("person income tax is=" , tax)



totalSecs = int(input("Enter seconds: "))

mins = totalSecs // 60
secs = totalSecs % 60

print(mins, "minutes and", secs, "seconds")
