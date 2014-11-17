def input_text():
    """Function for return input or default text"""
    a = raw_input("Enter the text. (Empty string == default text): ")
    if not a:
        a = """Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. \
Donec rutrum congue leo eget malesuada."""
#        a = "Mama mila ramu. A dolzna bila mit okno"
    return a


def input_int(message="Enter the number (positive integer): "):
    """Function for check and return input integer"""
    while True:
        a = raw_input(message)
        if a.isdigit():
            return int(a)
        else:
            print "Chto-to poshlo ne tak!!!"
