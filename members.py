'''

Quick and dirty script to grab members from propublica and dump
basic info into a local db
'''
import requests
from apikey import propublicakey
from dbconfig import *

def get_bill_info( rep ):
    base_url = "https://api.propublica.org/congress/v1/members/"+rep + "/bills/introduced.json"

    header_name = "X-API-Key"
    header = {header_name : propublicakey}

    r = requests.get(base_url, headers=header)

    return r

def get_bill_info_all_rep():
    #db.connect()
    for person in Rep.select():
        bills =  (get_bill_info( person.rep_id ).json()[ "results" ])[0]["bills"]
        for bill in bills:
            bill_list = [bill[ "number" ], bill["title"], bill["committees"], bill['introduced_date'], bill["bill_uri"]]
            add_bill( bill_list )
            print "Bill: ", bill["title"], " processed"
            
    #db.close()


def get_reps_info( legislative_house ):
    base_url = "https://api.propublica.org/congress/v1/"

    congress_number = "115"

    chamber = legislative_house

    all_mem_url = congress_number +"/"+chamber+"/members.json"

    header_name = "X-API-Key"

    header = {header_name : propublicakey}

    r = requests.get(base_url+all_mem_url, headers=header)
    return r


def jsonify_reps( r, legislative_house ):
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
        member_id = member[ "id" ]
        url = member["url"]

        info = [f_name, l_name, state, national_rep, house, party, member_id, url]
        members[x] = info

    return members

def load_members_db():
    s_members = jsonify_reps( get_reps_info("senate"), "senate" )
    c_members = jsonify_reps( get_reps_info("house"), "house" )
    
    create_tables()

    for member in s_members:
        add_rep( member )

    for member in c_members:
        add_rep( member )

try:
    load_members_db()
except e:
    print "exception: ", e
#get_bill_info_all_rep()
f = Bill.select()
print len(f), "  THIS MANY  "











