# mystery_set has been defined
string = input()

# delete string from mystery_set
try:
    mystery_set.remove(string)
except KeyError:
    pass
