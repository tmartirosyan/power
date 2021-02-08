def power(number: int, pow: int = 2) -> int:
    if pow == 1:
        return number
    else:
        return number * power(number, pow - 1)


print(power(3,3))