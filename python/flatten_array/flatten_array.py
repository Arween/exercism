new_array = []
def flatten(list_array):

    for arr in list_array:
        if isinstance(arr,int):
            new_array.append(arr)
        else:
            unpack_array(arr)
    return new_array

def unpack_array(temp_array):
    for arr in temp_array:
        new_array.append(arr)

