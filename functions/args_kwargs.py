# Using *args and **kwargs

def show_info(*args, **kwargs):
    # *args collects positional arguments into a tuple
    print("Args:", args)
    # **kwargs collects keyword arguments into a dictionary
    print("Kwargs:", kwargs)

show_info(1, 2, 3, name="John", age=25)
