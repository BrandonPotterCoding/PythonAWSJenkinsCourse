def fizz_buzz(ending):
    start = 0
    sum = 0
    while start<=ending:
        if start%15==0:
            print("Fizzbuzz")
        elif start%3==0:
            print("Fizz")
        elif start%5==0:
            print("Buzz")
        else:
            print(start)
            sum+=start
        start+=1
    print(sum)

amount = input("Enter in a number: ")
fizz_buzz(int(amount))