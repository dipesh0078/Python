#20.Write a function is_anagram(s1, s2) that checks if two strings s1 and
#s2 are anagrams of each other.

def is_anagram(s1,s2):
   s1=s1.replace(' ','').lower()
   s2=s2.replace(' ','').lower()
   return sorted(s1)==sorted(s2)



print(is_anagram('listen', 'silent'))        
print(is_anagram('triangle', 'integral'))    
print(is_anagram('hello', 'world'))           
print(is_anagram('Dormitory', 'Dirty room'))