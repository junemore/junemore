
def mean(num_list):
    """This is a docstring"""
    first = num_list[0]
    if isinstance(first, complex):
        return NotImplemented
    return sum(num_list)/len(num_list)