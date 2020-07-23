def fizzbuzz(num):
    num = int(num)
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    elif num % 5 == 0:
        output += "Buzz"
    elif len(output) == 0:
        output += str(num)
    return output
    
    # if num % 3 == 0 and num % 5 == 0:
    #     return "FizzBuzz"
    # elif num % 5 == 0:
    #     return "Buzz"
    # elif num % 3 == 0:
    #     return "Fizz"
    # else:
    #     return str(num)
