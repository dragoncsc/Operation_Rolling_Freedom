import requests
from apikey import propublicakey

base_url = "https://api.propublica.org/congress/v1/"

congress_number = "115"

chamber = "house"

all_mem_url = congress_number +"/"+chamber+"/members.json"

state = "ID"

district = "2"

mem_by_state = "members/"+chamber+"/"+state+"/"+district+"/current.json"

header_name = "X-API-Key"

header = {header_name : propublicakey}

r = requests.get(base_url+mem_by_state, headers=header)

raw_dict = r.json()

data_dict = None 
for key in raw_dict:
    if key == "results":
        data_dict = raw_dict[key][0]

if not data_dict:
    print "Error"

keys = ["name", "gender", "role", "party", "district", "id", "next_election", "seniority", "times_topics_url", "youtube_id", "twitter_id"]

for item in keys:
    value = data_dict[item]
    if value == '':
        value = "NA"
    print item + ": \t" + value

