#Import dependencies
import os
import csv
import datetime

#Dictionary to use for state abbreviations later. Used from [Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5)

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Define lists used in final output
f_name = []
l_name = []
dob_form = []
ssn_priv = []
empid = []
state_abb = []

#Define paths to both data csv and output csv

newemp = os.path.join("output","employee_summary.csv")
csvpath = os.path.join("employee_data.csv")

with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #Read in data to various lists for formatting purposes
    for row in csvreader:

        #Store empid for use later
        empid.append(row[0]) 

        #Define name to split below
        name = row[1]

        #Define DOB to reformat below
        dob = row[2]

        #Define SSN to reformat below
        ssn_raw = row[3]

        #Define state to use below
        full_state = row[4]

        #Split name into a list containing two items - first name and last name
        name_splitter = name.split()

        #Append first name and last name to separate lists above
        f_name.append(name_splitter[0])
        l_name.append(name_splitter[1])

        #Using DateTime module, convert the date column from a string into a date format, then reformat the date 
        dob_form.append(datetime.datetime.strptime(str(row[2]), '%Y-%m-%d').strftime('%m/%d/%Y'))

        #Split SSN on '-' and then choose the 3rd item in the new list to append to ***-**
        ssn_priv.append('***-**-' + ssn_raw.split("-")[2])

        #Using suggested state dictionary, use the full state provided to get state abbreviations
        state_abb.append(us_state_abbrev.get(full_state))

#Write newly formatted data to a new CSV
with open(newemp, "w", newline="") as datafile:
    writer = csv.writer(datafile)

#Write Header Row
    writer.writerow(["Emp ID","First Name","Last Name","DOB", "SSN","State"])

#Write data rows, looping through lists above to fill columns
    for x in range(0,len(f_name)):
        writer.writerow([empid[x], f_name[x], l_name[x], dob_form[x], ssn_priv[x], state_abb[x]])