import statistics

number_1 = int(input("Enter number 1:"))
number_2 = int(input("Enter number 2:"))
number_3 = int(input("Enter number 3:"))
number_4 = int(input("Enter number 4:"))

def is_prime(input_number):
    i = 2
    if input_number <= 1:
        print("not prime")
        return
    elif input_number == 2:
        print("prime")
        return
    while i < input_number:
        modulo = input_number % i
        if modulo == 0:
            print("not prime")
            break;
        if(i == input_number - 1):
            print("prime")
        i += 1
        

is_prime(number_1)
is_prime(number_2)
is_prime(number_3)
is_prime(number_4)

def is_median(number_1, number_2, number_3, number_4):
    median_value = statistics.median([number_1, number_2, number_3, number_4]) 
    print(f"Median is {median_value}.")

is_median(number_1, number_2, number_3, number_4)


