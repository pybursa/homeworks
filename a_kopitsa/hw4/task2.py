text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada."


def myfunction(limit):
    count = limit
    if text[limit:limit+1] == " ":
        print text[:limit]
    elif text[limit:limit+1] == ".":
        print text[:limit] + "."
    else:
        while not (text[limit:limit+1] == "." or text[limit:limit+1] == " "):
            limit += 1
        if " " in text[:limit]:
            print text[:limit] + "..."
        else:
            print text[:count] + "..."

myfunction(24)
myfunction(23)
myfunction(13)
myfunction(6)
myfunction(3)
