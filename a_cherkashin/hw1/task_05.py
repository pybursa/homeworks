def typer(arg):
    return type(arg).__name__
    
print 'typer(66): ' + typer(66)
print 'typer("66"): ' + typer("66")
print 'typer(typer): ' + typer(typer)
