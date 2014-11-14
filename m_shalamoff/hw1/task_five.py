__author__ = 'm_shalamov'


def typer(item):
    if type(item) is int:
        print '"int"'
    elif type(item) is str:
        print '"str"'
    elif type(item) is type(typer):
        print '"function"'
    else:
        print "Can not define object type"


if __name__ == '__main__':
    typer(666)
    typer('666')
    typer(typer)
    typer([])