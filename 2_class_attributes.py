from congress import ElectedOfficial

# e = ElectedOfficial()
# e.parties

assert ["D", "R", "I"] == ElectedOfficial.parties


# if you see the name of the class on the left of the dot, then you don't need to specify what its passing in
# basically, for class level stuff, you don't need "self"
# for instance level, you need "self"
representatives = ElectedOfficial.get_all()
assert type(representatives) is list
assert 442 == len(representatives)

illinois_delegation = ElectedOfficial.get_all_from_state("IL")
assert type(illinois_delegation) is list
assert 18 == len(illinois_delegation)
assert "IL" == illinois_delegation[0].state
print("AWESOME")
