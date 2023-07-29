def main():
    #cycle through from 1 to 100
    for i in range(1, 101):
        #if number if divisible by both 3 and 5, print fizzbuzz
        if i % 15 == 0:
            print(i , " FIZZBUZZ")
        #or if the number is divisible by 3 and not 5, print fizz
        elif i % 3 == 0:
            print(i , " FIZZ")
        #or if the number is divisible by 5 and not 3, print buzz
        elif i % 5 == 0:
            print ( i , " BUZZ")
        else:
            #finally, if it is not divisible by any of the numbers 3 or 5, just print the number as it is
            print(i)

if __name__ == "__main__":
    main()
