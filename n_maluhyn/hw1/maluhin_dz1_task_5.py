__author__ = 'maln'

# Return type name.
# @param str text
def typer(obj):
    return type(obj).__name__

print typer(666)
print typer("666")
print typer(typer)