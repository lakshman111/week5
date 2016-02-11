# Thanks to the NY Times API: http://developer.nytimes.com/docs

import json

# This class will (eventually) represent one member of Congress.
class ElectedOfficial:
  # need to have something here, so include pass if nothing else
  # pass

  # this is a class level attribute
  parties = ["D", "R", "I"]

  def get_all_from_state(state):
    with open("congress.json", encoding='utf-8') as f:
  # sets f = to open("congress.json", encoding='utf-8')
  # also, this automatically closes the file outside of the with/as clause
     data = json.load(f)

    rep_data = data["results"][0]["members"]

    member_list = []

    for person in rep_data:
      new_member = ElectedOfficial()
      new_member.name = "Last Name:{0}, First Name:{1}".format(person["last_name"], person["first_name"])
      new_member.party = person["party"]
      new_member.state = person["state"]

      if "votes_with_party_pct" in person:
        # some members do not have this info listed
        new_member.loyalty_factor = float(person["votes_with_party_pct"])
      else:
        new_member.loyalty_factor = 0.0

      if new_member.state == state:
        member_list.append(new_member)

    return member_list

  def print_summary(self):
    print(self.name)
    print(self.party)

  def get_all():
    with open("congress.json", encoding='utf-8') as f:
    # sets f = to open("congress.json", encoding='utf-8')
    # also, this automatically closes the file outside of the with/as clause
      data = json.load(f)

    rep_data = data["results"][0]["members"]

    member_list = []

    for person in rep_data:
        new_member = ElectedOfficial()
        new_member.name = "Last Name:{0}, First Name:{1}".format(person["last_name"], person["first_name"])
        new_member.party = person["party"]
        new_member.state = person["state"]

        if "votes_with_party_pct" in person:
          # some members do not have this info listed
          new_member.loyalty_factor = float(person["votes_with_party_pct"])
        else:
          new_member.loyalty_factor = 0.0

        member_list.append(new_member)

    # could store by doing ElectedOfficial.memberlist = member_list
    # then you can access from get_all_from_state
    return member_list



# This function reads from congress.json
# and returns a list of members of congress
# who have been in office long enough to
# have voted on a bill at least once.
# Also, can you spot two design patterns? map and then reduce

# We create a class with attributes so that we only have the stuff that we care about
# Changed it to def getall(): to do 2_class_attributes.py

def read_from_file():
  with open("congress.json", encoding='utf-8') as f:
    # sets f = to open("congress.json", encoding='utf-8')
    # also, this automatically closes the file outside of the with/as clause
    data = json.load(f)

  rep_data = data["results"][0]["members"]

  member_list = []

  for person in rep_data:
      new_member = ElectedOfficial()
      new_member.name = "Last Name:{0}, First Name:{1}".format(person["last_name"], person["first_name"])
      new_member.party = person["party"]
      new_member.state = person["state"]

      if "votes_with_party_pct" in person:
        # some members do not have this info listed
        new_member.loyalty_factor = float(person["votes_with_party_pct"])
      else:
        new_member.loyalty_factor = 0.0

      member_list.append(new_member)

  return member_list
