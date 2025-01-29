
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""

    inc = True
    dec = True 
    firstnum = lst[0]

    for num in lst[1:]:
        if firstnum > num:
            inc = False     
        else:
            dec = False
        firstnum = num 

    if inc or dec:
        return True
    else:
        return False 
  
test1 = [0, 1, 2, 3]
test2 = [1,1,3,100]
test3 = [11, 1,-9,-10]
test4 = [2,3,2,3]
print(monotonic(test1))
print(monotonic(test2))
print(monotonic(test3))
print(monotonic(test4))