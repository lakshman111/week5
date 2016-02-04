# More practice with constructors
from congress import ElectedOfficial

data = { "id": "D000622", "thomas_id": "2123",
         "api_uri": "http://api.nytimes.com/svc/politics/v3/us/legislative/congress/members/D000622.json",
         "first_name": "Tammy", "middle_name": None,
         "last_name": "Duckworth", "party": "D",
         "twitter_account": "RepDuckworth", "facebook_account": "CongresswomanTammyDuckworth",
         "facebook_id": "112300955610529", "url": "http://duckworth.house.gov",
         "rss_url": "http://duckworth.house.gov/rss.xml",
         "domain": "duckworth.house.gov", "dw_nominate": "-0.274",
         "ideal_point": "-0.680333034", "seniority": "2",
         "state": "IL", "district": "8", "missed_votes_pct": "6.54",
         "votes_with_party_pct": "89.41"
        }

rep_duckworth = ElectedOfficial(data)

assert rep_duckworth.party == 'D'
assert rep_duckworth.loyalty_factor == 89.41

print("All assertions passed!")
