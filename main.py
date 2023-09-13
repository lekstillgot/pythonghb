# import module

# print(module.calculator.plus(3, 5))
# print(module.number.factorial(3))
# from module import calculator, number
# print(calculator.plus(3, 5))
# print(number.factorial(3))

from module import calculator as cal, number as num
print(cal.plus(3, 5))
print(num.factorial(10))
