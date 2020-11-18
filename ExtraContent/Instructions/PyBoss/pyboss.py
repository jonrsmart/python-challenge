# First we’ll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
import datetime

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

f_name = []
l_name = []
dob_form = []
ssn_priv = []
empid = []
state_abb = []

csvpath = os.path.join("employee_data.csv")

with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    for row in csvreader:
        empid.append(row[0])
        name = row[1]
        dob = row[2]
        ssn_raw = row[3]
        full_state = row[4]

        name_splitter = name.split()
        f_name.append(name_splitter[0])
        l_name.append(name_splitter[1])
        dob_form.append(datetime.datetime.strptime(str(row[2]), '%Y-%m-%d').strftime('%m/%d/%Y'))
        ssn_priv.append('***-**-' + ssn_raw.split("-")[2])
        state_abb.append(us_state_abbrev.get(full_state))

for x in range(0,len(f_name)):
    print(f'{f_name[x]} {l_name[x]} {dob_form[x]} {ssn_priv[x]} {empid[x]} {state_abb[x]}')