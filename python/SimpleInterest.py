# Simple Interest Calculator
# Input: Loan Amount, Duration, Interest
#amount = input("What is the loan amount? ")
#years = input("What is the duration in years? ")
#apr = input("What is the yearly interest? ")
#print("So, you are already " + str(age) + " years old, " + name + "!")
amount = 100000
years=30
rate= .1

print("Balance: " + str(amount))
print("Interest Rate: " + str(rate))
print("Duration(Years): " + str(years))

for x in range(1,years+1):
    interest = x*(amount*rate)
    total = amount + interest
    print("Year Number: " + str(x))
    print("  Interest Charge this Year: " + str(interest))
    print("  Total You Owe: " + str(total))

    
