def fizzbuzz(num):
    if num % 3 == 0:
        return "Fizz"
    elif num == 5:
        return "Buzz"
    elif num == 15:
        return "FizzBuzz"
    else:
        return str(num)
