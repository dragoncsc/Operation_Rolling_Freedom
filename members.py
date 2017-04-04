import requests
from apikey import propublicakey

base_url = "https://api.propublica.org/congress/v1/"

congress_number = "115"

chamber = "senate"

all_mem_url = congress_number +"/"+chamber+"/members.json"

header_name = "X-API-Key"

header = {header_name : propublicakey}

r = requests.get(base_url+all_mem_url, headers=header)

raw_dict = r.json()

data_dict = None

for key in raw_dict:
    if key == "results":
        data_dict = raw_dict[key][0]

for key in data_dict = 
