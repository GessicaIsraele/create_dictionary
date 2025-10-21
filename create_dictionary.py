
def create_dictionary(*args) -> dict:
    new_dict = {}
    for i, arg in enumerate(args):
        if isinstance(arg, (list, set, dict)):
            print(f"Cannot add {arg} to the dict!")
        else:
            new_dict[arg] = i
    return new_dict
