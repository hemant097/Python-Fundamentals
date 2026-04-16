#python compound interest calculator

principal=0
rate = 0
time = 0

while True:
    principal = float(input("Enter a principle amount: "))
    if principal < 0:
        print("Principal can only be a positive number")
    else: break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate can only be a positive number")
    else: break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can only be a positive number")
    else:
        break

print(principal)
print(rate)
print(time)

total = principal* pow( (1+rate/100),time);
print(f"balance after {time} years: ${total:.2f}  ")