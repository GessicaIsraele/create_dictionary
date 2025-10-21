def create_dictionary(*args):
    new_dict = {}
    for i, arg in enumerate(args):
        if isinstance(arg, (int, float, str, bool, tuple, type(None))):
            new_dict[arg] = i
        elif callable(arg):
            new_dict[arg] = i
        else:
            print(f"Cannot add {arg} to the dict!")
    return new_dict
