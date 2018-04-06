import operator
from itertools import zip_longest
def clean_prison_data(prison_data_file_name,cleaned_prison_data_file_name):
    with open(prison_data_file_name, 'r') as prisonfile,open(cleaned_prison_data_file_name,"w") as outfile:
        outfile.write("state,year,people\n")
        i = 0
        list_of_lines = prisonfile.readlines()
        list_of_lines.sort()
        for line in list_of_lines:
            values = line.split(',')
            if values[2]=="Total":
                outfile.write(values[0].upper() + ',' + values[1] + ',' + values[17])

def clean_crime_data(crime_data_file_name,cleaned_crime_data_file_name):
    with open(crime_data_file_name, 'r') as crimefile,open(cleaned_crime_data_file_name,"w") as outfile:
        outfile.write("state,year,people\n")
        i = 0
        ans=0
        list_of_lines = crimefile.readlines()
        list_of_lines.sort()
        for line in list_of_lines:
            values = line.split(',')
            if values[1]=="TOTAL":
                outfile.write(values[0] + ',' + values[2] + ',' + values[32])
            if values[1]=="TOTAL" and values[2]=="2005":
                ans += int(values[32])
        print("LOL" + str(ans))

def get_combined_data(cleaned_crime_data_file_name,cleaned_prison_data_file_name, total_crime_data_file_name):
    with open(cleaned_prison_data_file_name,"r") as prisonfile,open(cleaned_crime_data_file_name,"r") as crimefile,open(total_crime_data_file_name,"w") as outfile:
        i=0
        ans = 0
        prisonfiledata = {}
        crimefiledata = {}
        states = set()
        years = set()
        outfile.write("state,year,people_in_prison,crimes_reported\n")
        for line in prisonfile:
            if i==0:
                i+=1
                continue
            values = line.split(',')
            prisonfiledata[(values[0],values[1])] = values[2].rstrip('\n')
            states.add(values[0])
            years.add(values[1])
        for line in crimefile:
            if i==1:
                i+=1
                continue
            values = line.split(',')
            crimefiledata[(values[0],values[1])] = values[2].rstrip('\n')
            states.add(values[0])
            years.add(values[1])
        for state in states:
            for year in years:
                if (state,year) in prisonfiledata and (state,year) in crimefiledata:
                    outfile.write(state + "," + year + "," + prisonfiledata[(state,year)] + "," + crimefiledata[(state,year)] + '\n')
                elif (state,year) in prisonfiledata:
                    outfile.write(state + "," + year + "," + prisonfiledata[(state,year)] + ",0\n")
                elif (state,year) in crimefiledata:
                    outfile.write(state + "," + year + ",0," + crimefiledata[(state,year)] + '\n')
        print(ans)
            
        

prison_data_file_name = "data_prison.csv"
cleaned_prison_data_file_name = "clean_prison_data.csv"
crime_data_file_name = "data_crime.csv"
cleaned_crime_data_file_name = "clean_crime_data.csv"

clean_crime_data(crime_data_file_name,cleaned_crime_data_file_name)
clean_prison_data(prison_data_file_name, cleaned_prison_data_file_name)
get_combined_data(cleaned_crime_data_file_name, cleaned_prison_data_file_name, "total_cleaned_data.csv")
