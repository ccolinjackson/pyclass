name = 'Chris C. Jackson'
age = 52 # accurate at the time
height = 74 # inches
weight = 206 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'
centimeters = height * 2.54
kilograms = weight * .453592
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That's %d in centimeters." % centimeters
print "He's %d pounds heavy." % weight
print "Or %d in kilos." % kilograms
print "Actually, that's not too bad."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on if he's brushed this morining." % teeth

print "If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)
