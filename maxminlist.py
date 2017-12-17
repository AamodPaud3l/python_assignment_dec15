#Program to find maximum and minimum number from the list
my_list = [4,2,4,0,2,4,5,7,8,9,23,8,5,4,2,2,34,4,45]
my_list.sort()
minimum = my_list[0]
print("Minimum number is: {}".format(minimum))
my_list.reverse()
maximum = my_list[0]
print("Maximum number is: {}".format(maximum))