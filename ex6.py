# x represents a variable that contains a string
# %d represents the number 10. #
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# %s is for the two string variables
y = "Thise who know %s and those who %s." % (binary, do_not)

print x
print y

# %r can be used for debugging
print "I said: %r" % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
