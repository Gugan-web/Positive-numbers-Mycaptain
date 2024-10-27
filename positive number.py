
def filter_positive_numbers(numbers):
    positive_numbers = []   
    for num in numbers:  
        if num > 0:  
            positive_numbers.append(num)   
    return positive_numbers


input_list = []  


n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    number = int(input("Enter number {}: ".format(i + 1)))  # Ask user to enter a number
    input_list.append(number)  

positive_numbers = filter_positive_numbers(input_list)

print("Positive numbers in the list are:", positive_numbers)
