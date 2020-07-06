def convert_to_numeric(func):
    # define a function within the outer function
    def new_func(x):
        return func(float(x))
    # return the newly defined function
    return new_func
