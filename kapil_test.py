'''
1. Write a function to write a max value in the given list
2. Write a function to remove duplicate from the given list
3. Write a function to combine given two dictionaries
4. Write a function to print all odd numbers in a given list.
5. Write a function to print all prime numbers in the given list
'''

list_1 = [23, 11, 45, 34, 5, 567, 44, 43, 22, 84]
dic_1 = {"name": "Kapil", "age": "25"}
dic_2 = {"position": "Data Engineer", "Company": "CareerSoft"}
list2 = []
list3 = []
def max_value(list_1):
    count = list_1[0]

    for i in range(len(list_1)):
        if list_1[i] > count:
            count = list_1[i]
    return count


print(max_value(list_1))


def remove_dup(list_1):
    list_2 = list(set(list_1))
    return list_2


print(remove_dup(list_1))


def com_dictionary(dic_1, dic_2):
    dic_1.update(dic_2)
    return dic_1
print(com_dictionary(dic_1,dic_2))

def odd_no(list_1):
    for i in list_1:

        if i % 2 != 0:
            list2.append(i)
    return list2
print(odd_no(list_1))

def prime_no(list_1):
    for num in list_1:
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list3.append(num)
    return(list3)

print(prime_no(list_1))