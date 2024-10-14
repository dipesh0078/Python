#38.Write a function concatenate_strings(*args) that concatenates an arbitrary number of strings.

def concatenate_strings(*args):
    final=''
    for i in args:
        final=final+' '+i
    return final

result = concatenate_strings("Hello","world", "!", "How", "are", "you?")
print(result)  # Output: "Hello world! How are you?"