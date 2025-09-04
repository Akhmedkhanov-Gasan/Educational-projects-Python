def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        else:
            return True
    else:
        return False


result = is_prime(79701)
print(result)