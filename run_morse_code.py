from package_i.code_morse import *


a1 = get_morse_sentence('this-is-my-first-visit!')
a2 = get_morse_sentence('033213-2423187-1912374')
print( "%s\n%s"%(a1,a2) )
print()

d1 = get_english_sentence(a1)
d2 = d = get_english_sentence(a2)
print("%s\n%s"%(d1,d2))
print()


c = get_morse_chart()
print(c)


print('\t------ VERIFICATION --------')
b1 = get_morse_sentence("'-27?ejoty")
b2 = get_morse_sentence("(.38afkpuz")
b3 = get_morse_sentence(")/49bglqv")
b4 = get_morse_sentence("+05:chmrw")
b5 = get_morse_sentence(",16=dinsx")
print("%s\n%s\n%s\n%s\n%s"%(b1,b2,b3,b4,b5))
print()

d1 = get_english_sentence(b1)
d2 = get_english_sentence(b2)
d3 = get_english_sentence(b3)
d4 = get_english_sentence(b4)
d5 = get_english_sentence(b5)
print("%s\n%s\n%s\n%s\n%s"%(d1,d2,d3,d4,d5))
print()
print('\t-----------------------------')


print(get_english_sentence('..-. .-'))
