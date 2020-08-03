largest = 0
smallest = 0
numbers = []

userInput = int(input("Enter a range: "))

while True:
    for number in range(userInput):
        data = input("Enter a number: ")
        if data == 'done':
            break
        try:
            newData = int(data)
        except:
            print('Invalid input')
            continue

        numbers.append(newData)
        numbers.sort()

    largest = numbers[0]
    smallest = numbers[0]

    for num_01 in numbers:
        if num_01 > largest:
            largest = num_01

    for num_02 in numbers:
        if num_02 < smallest:
            smallest = num_02

    print("Maximum", largest)
    print("Minumun", smallest)
    quit()
