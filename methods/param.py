def increment(number, by):
    return number + by


result = increment(2, 1)

print(result)

# default params


def increment(number, by=1):
    return number + by


print(increment(1))

print(increment(3, 3))


def multiply(*numbers):
    print(numbers)


print(2, 4, 4, 4)


def multiply(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(multiply(4, 4, 4, 4))


def save_user(**user):
    print(user)

save_user(id=1, name="john", age=22)
