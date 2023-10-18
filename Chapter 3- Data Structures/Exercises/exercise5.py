family=['Shaan','Baiju','Grace']
msg=("I'd like to invite ")+family[0].title()+(", to dinner")
print(msg)
msg=("I'd like to invite ")+family[1].title()+(", to dinner")
print(msg)
msg=("I'd like to invite ")+family[2].title()+(", to dinner")
print(msg)

msg=("Sorry,")+family[1].title()+(" cannot come for dinner")
print(msg)

del(family[1])
family.insert(1,'eva')

msg=("I'd like to invite ")+family[0].title()+(", to dinner")
print(msg)
msg=("I'd like to invite ")+family[1].title()+(", to dinner")
print(msg)
msg=("I'd like to invite ")+family[2].title()+(", to dinner")
print(msg)