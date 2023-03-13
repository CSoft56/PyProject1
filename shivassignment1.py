
testlist = [1, 2, 3, 4, 2, 6, 6, 8]

"""
write a function to find max value in given list
"""
def highnumber(testlist):
    highvalue = max(testlist)
    return highvalue
h = highnumber(testlist)
print("The maximum value in given list is:",h)

"""
write  a function to remove duplicates from a given list

"""
def dupremove(testlist):
    newlist = set(testlist)
    return newlist
n = dupremove(testlist)
print("The new list after removing duplicates is:", n)

"""
write  a function to print all odd numbers in given list

"""
def alloddnum(testlist):
    oddlist =[]
    for number in testlist:
        if number % 2 != 0:
         oddlist.append(number)


    return oddlist

o = alloddnum(testlist)
print(o)

"""
write  a function to print all prime numbers in given list

"""
def allprimenum(testlist):
    primelist =[]
    for number in testlist:
        if number % 1 == 0:
            primelist.append(number)


    return primelist

p = allprimenum(testlist)
print(p)

"""
write  a function to combine given two dictionaries and return

"""

patients1 = {"erica": "xavier", "yash": "gupta"}
patients2 = {"david": "kaufman", "aimee": "afable"}

def combinedic(patients1, patients2):
    newdic = {**patients1, **patients2}
    return newdic

patients = combinedic(patients1, patients2)
print(patients)
