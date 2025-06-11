# Создали модуль main
"""num = 600851475143

    primes=[2]
    result_max = num//3
    temp = 2

    while temp < result_max:
        temp  += 1
        # проверка числа на простату
        flag = True
        for prime in primes:
            flag *= temp%prime
        if flag:
            #print(temp)
            primes.append(temp)

            if num%temp == 0:
                result = temp
                print(result)

    #print(result)




def PrimeFactors(n):
    divisor = 2
    l = []
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            l.append(divisor)
            #print(n)
        else:
            divisor += 1
            #print(divisor)
    if n != 1:
        l.append(n)
    print(*l)
    return l

if __name__ == '__main__':
    print(max(PrimeFactors(600851475143)))

 
 
 """
 #Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

n = 4000000
fib = [1, 2]
fib_even = [2]

while fib[-1] < n:
    new_fib = fib[-1]+fib[-2]
    fib[-2] = fib[-1]
    fib[-1] = new_fib
    if new_fib%2 == 0: fib_even.append(new_fib)

#print(len(fib_even))
print(*fib_even)
print(sum(fib_even))
