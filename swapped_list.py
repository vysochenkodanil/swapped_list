def bubble_sort(data):
    last_index = len(data) - 1
    swapped = True
    while swapped:
        swapped = False
        for item_index in range(last_index):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = data[item_index + 1], data[item_index]
            swapped = True
        last_index -=1
    return  data