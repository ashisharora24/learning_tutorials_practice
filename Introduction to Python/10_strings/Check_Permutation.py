# Check Permutation

# Given two strings, check if they are permutations of each other.
# Return true or false.
# Permutation means - length of both the strings should same and should contain same set of characters.
# Order of characters doesn't matter.
# Note : Input strings contain only lowercase english alphabets.
# Input format :
# Line 1 : String 1
# Line 2 : String 2
# Sample Input 1 :
# abcde
# baedc
# Sample Output 1 :
# true
# Sample Input 2 :
# abc
# cbd
# Sample Output 2 :
# false

def check(str1,str2):
    ref_holder={}
    for i in str1:
        if i not in ref_holder:
            ref_holder[i]=0
        index = str2.find(i,ref_holder[i])
        if index != -1:
            ref_holder[i]=index
        else:
            break
    else:
        return True
    return False

def check_permutation(str1,str2):
    # val2 = check(str2,str1)
    # val1 = check(str1,str2)
    if (check(str1,str2) and check(str2,str1)):
        return True
    else:
        return False

print(check_permutation(input(),input()))
