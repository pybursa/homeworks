def is_sym(string):
    return string == string[::-1]
  
print "abba is " + str(is_sym("abba"))
print "arbat is " + str(is_sym("arbat"))
print "abdba is " + str(is_sym("abdba"))