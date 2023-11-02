def list_op(my_list, index, operation):
    try:
        result = operation(my_list[index])
        return result
    except IndexError:
        return None

my_list = [1, 2, 3, 4, 5]

index = 10
operation = lambda x: x * 2 

result = list_op(my_list, index, operation)

if result is not None:
    print("Result: {result}")
else:
    print("Index is out of range.")
