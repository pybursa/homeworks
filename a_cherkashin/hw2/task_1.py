def return_double(enum):
    enum_tuple = False
    if enum.__class__ is tuple:
        enum_tuple = True
    new_enum = map(lambda x: x ** 2, enum)
    if enum_tuple:
        return tuple(new_enum)
    else:
        return new_enum
      
print return_double([1,2,3])
print return_double((1,2,3))