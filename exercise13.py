# format specifiers

price1 = 3.14159
price2 = -987.54
price3 = 12.34

print(f"The price1 is Rs {price1}.")
print(f"The price2 is Rs {price2}.")
print(f"The price3 is Rs {price3}.")

print("\ndecimal formatting")

print(f"The price1 is {price1:.2f}")
print(f"The price2 is {price2:.3f}")
print(f"The price3 is {price3:.4f}")

print("\neach value holds 10 character space")

print(f"The price1 is {price1:10}")
print(f"The price2 is {price2:10}")
print(f"The price3 is {price3:10}")

print("\npadding formatting")

print(f"The price1 is {price1:010}")
print(f"The price2 is {price2:010}")
print(f"The price3 is {price3:010}")

print("\nleft justified")

print(f"The price1 is Rs {price1:<10}")
print(f"The price2 is Rs {price2:<10}")
print(f"The price3 is Rs {price3:<10}")

print("\nright justified")

print(f"The price1 is {price1:>10}")
print(f"The price2 is {price2:>10}")
print(f"The price3 is {price3:>10}")

print("\n centre align")

print(f"The price1 is {price1:^10}")
print(f"The price2 is {price2:^10}")
print(f"The price3 is {price3:^10}")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

print(f"The price1 is {price1:}")
print(f"The price2 is {price2:}")
print(f"The price3 is {price3:}")

print("\n positive negative sign")

print(f"The price1 is {price1:+}")
print(f"The price2 is {price2:+}")
print(f"The price3 is {price3:+}")

print("\n only negative sign")

print(f"The price1 is {price1: }")
print(f"The price2 is {price2: }")
print(f"The price3 is {price3: }")

print("\nthousand separator")

num1 = 464646464615.1
num2 = -413431.2554
num3 = 1523

print(f"The price1 is {num1:,}")
print(f"The price2 is {num2:,}")
print(f"The price3 is {num3:,}")

print("\n mixing different ")

print(f"The price1 is {price1:+,.2f}")
print(f"The price2 is {price2: ,.3f}")
print(f"The price3 is {price3:+,.6f}")





