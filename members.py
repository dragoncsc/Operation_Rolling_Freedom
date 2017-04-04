'''

Quick and dirty script to grab members from propublica and dump
basic info into a local db
'''
import requests
from apikey import propublicakey
from dbconfig import *

def get_reps_info():
    base_url = "https://api.propublica.org/congress/v1/"

    congress_number = "115"

    chamber = "senate"

    all_mem_url = congress_number +"/"+chamber+"/members.json"

    header_name = "X-API-Key"

    header = {header_name : propublicakey}

    r = requests.get(base_url+all_mem_url, headers=header)
    return r


def jsonify_reps( r ):
    raw_dict = r.json()

    data_dict = None

    for key in raw_dict:
        if key == "results":
            data_dict = raw_dict[key][0]

    members_list = data_dict["members"]

    #Initalize cause im a basic betch
    members = [None]*len(members_list)

    chamber = "senate"

    for x in xrange(len(members_list)):
        member = members_list[x]
        f_name = member["first_name"]
        l_name = member["last_name"]
        state = member["state"]
        national_rep = True
        house = chamber
        party = member["party"]
        
        info = [f_name, l_name, state, national_rep, house, party]
        members[x] = info

    return members

def load_members_db():
    members = jsonify_reps( get_reps_info() )

    create_tables()

    for member in members:
        add_rep( member )
        print member[0]
        print member[1]
        print member[2]
        print member[3]
        print member[4]
        print member[5]
        print '\n\n'

load_members_db()













