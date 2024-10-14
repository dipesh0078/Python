#17.Write a function longest_word(words) that returns the longest word
#from a list of words.

def longest_word(words):
    temp=''
   
    for i in words:
        if len(i)>len(temp):
            temp=i
    return temp

string=['aba','asdasd','a','agas','adsa']

print(longest_word(string))