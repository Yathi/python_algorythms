arrInput = int(input("Enter number of elements:"))

inputs = list(range(arrInput))

print(inputs)

exit = False

def union(first, second):
    pid = inputs[first]
    qid = inputs[second]
    if pid == qid:
        print('They are already connected. Nothing to do')
    else:
        for i in range(arrInput):
            if inputs[i] == qid:
                inputs[i] = pid


def find(first, second):
    pid = inputs[first]
    qid = inputs[second]
    if pid == qid:
        print('Connected')
    else:
        print('No bueno')


while not exit:
    option = int(input('Enter an option: 1 - exit, 2-union, 3-find, 4-print: '))

    if option == 1:
        exit = True
        break
    elif option == 4:
        print(inputs)
    else:
        first = int(input('Enter first number: '))
        second = int(input('Enter second number: '))

        if option == 2:
            union(first, second)
        elif option == 3:
            find(first, second)
        else:
            print('Invalid input')

