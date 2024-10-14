#40.Write a function combine_args_kwargs(*args, **kwargs) that prints
#all positional arguments and keyword arguments passed to it.

def combine_args_kwargs(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


combine_args_kwargs(1, 2, 3, name="Aman", age=30, city="ktm")
