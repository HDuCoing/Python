file = open("example_sorted_names.txt")
name_list = []
for line in file:
    line=line.strip()
    name_list.append(line)

def binary_search(the_list, item):
    lower = 0
    upper = len(the_list) - 1
    while True:
        if upper < lower:
            return -1
        middle = (lower + upper) // 2
        if the_list[middle][0] < item:
            lower = middle + 1
        elif the_list[middle][0] > item:
            upper = middle - 1
        else:
            return middle
def names_beginning(the_list,item):
    index=0
    while True:
        index=binary_search(the_list,item)
        if index!=-1:
            print(name_list[index])
        else:
            break
        del name_list[index]

names_beginning(name_list,"S")