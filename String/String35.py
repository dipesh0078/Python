#Write a Python program to replace every second
#character of a string with *.


original_string = input("Enter your string: ")
result_string = ""
for index in range(len(original_string)):
    if index % 2 == 1:  
        result_string += '*'  
    else:
        result_string += original_string[index]  

print("Modified string:", result_string)