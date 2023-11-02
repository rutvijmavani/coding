def right_rotate_array(arr, D):
    D = D % len(arr)
    
    arr[:D], arr[D:] = arr[-D:][::-1], arr[:-D][::-1]
    
arr = [1, 2, 3, 4, 5]
D = 2

right_rotate_array(arr, D)

print("arr after rotation =", arr)
