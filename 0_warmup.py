import congress

# Congressional representatives have properties like:
# - name
# - party
# - state
# - loyalty_factor (% of votes with their party)
#
# See the congress.py file for more details.

representatives = congress.read_from_file()

### Can you write code to display the correct answers?


# 1. What type of object is held inside the 'representatives' variable?

print(type(representatives))


# 2. How many representatives are there?
print(len(representatives))


# 3. Display the name of the last representative.
print(representatives[-1].name)


# 4. Which rep is most loyal to their party?
loyalty = 0
most_loyal = representatives[0].name
for person in representatives:
  if person.loyalty_factor > loyalty:
    most_loyal = person.name
    loyalty = person.loyalty_factor
print(most_loyal)


# 5. Which rep is a traitor to their party?
# some people have an entry of 0, so make sure to ignore those


# 6. Can you make the following code work?
#    You can modify the congress.py file if you want to.

first_rep = representatives[0]
print(first_rep.print_summary())

#    should display:
#
#    Robert, Aderholt. Republican.
