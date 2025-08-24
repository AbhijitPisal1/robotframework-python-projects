# Question: From the given string remove all integers and also return the count of occurence for each character in string
str1 = "fghbd7837bd58ehbdu6wdi26w2hd96wd2h"


def remove_num_from_string(str1):
    str2 = ""
    for ch in str1:
        if not ch.isdigit():
            str2 += ch
            
    print(str2)
    
    count_freq={}
    for char in str2:
        if char in count_freq:
            count_freq[char] += 1
        else:
            count_freq[char] = 1
    print(count_freq)
      
remove_num_from_string(str1)
            