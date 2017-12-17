#Program to cube each elements in a list and append it to another list
list = [1,2,4,4,3,5,6]

def cube_list(arbitary_list):
    new_list = []
    for each in arbitary_list:
        each = each ** 3
        print(each)
        new_list.append(each)
    new_list1 = [7,8,9]
    new_list.append(new_list1)
    print(new_list)

cube_list(list)
