#Given a string containing special characters like
#newline (\n), tab (\t), and backslash (\\), escape the
#characters properly.


original_string = "Hello\nWorld!\tThis is a backslash: \\"


escaped_string = repr(original_string)

print("Original String:")
print(original_string)

print("\nEscaped String:")
print(escaped_string)