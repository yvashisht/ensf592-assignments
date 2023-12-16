# calgary_dogs.py
# AUTHOR NAME Yajur Vashisht
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

# Importing both Numpy and Pandas for the assignment

import numpy as np
import pandas as pd 

def main():

    # Imported data
    data = pd.read_excel(r'/Users/yajurvashisht/Documents/GitHub/assignment4calgarydogsp23-yvashisht/CalgaryDogBreeds.xlsx')

    print("ENSF 592 Dogs of Calgary")
        
    # User input stage
    while True:
        breed = input("Please enter a dog breed: ") #user inputs breed
        try:
            breed_data = data[data['Breed'].str.lower() == breed.lower()] #makes everything lowercase so it is not case-sensitive
            if breed_data.empty:
                raise ValueError
            break
        except ValueError:
            print("Dog breed not found in the data. Please try again.") #raises value error if a correct input is not inputted

    # Data anaylsis stage

    #Determines the years that the breed appears in the top dog breeds csv
    data_year = breed_data['Year'].unique()
    print("The {} was found in the top breeds for years:".format(breed.upper()), *data_year)
    #Finds the total of the dog breed in the csv
    data_total_reg = breed_data['Total'].sum()
    print("There have been", data_total_reg,"{} dogs registered total.".format(breed))
    #Finds the total of the dog breed per year in the csv
    breed_totals = breed_data.groupby('Year')['Total'].sum()
    breed_totals = pd.DataFrame(breed_totals)
    df = pd.MultiIndex.from_frame(breed_totals)
    print(df)
    # breed_totals_multi = pd.MultiIndex.from_tuples(breed_totals)
    # print(breed_totals_multi)
    #Finds the total of ALL dog breed per year in the csv
    year_reg = data.groupby('Year')['Total'].sum()
    #Finds the perentage per year of each dog breed over the total dog registrations
    breed_per_total = (breed_totals/year_reg)
    breed_per_total = breed_per_total.fillna(0)

    #Determines the months that were the most popular for the inputted dog breed. 
    popular_months = breed_data.groupby('Month').size()
    max_count = popular_months.max()
    #Filters out unpopular months by using a mask
    popular_months = popular_months[popular_months >= max_count]

    #Print statments for the desired statistics
    print("The {} was".format(breed.upper()),f"{breed_per_total.iloc[0]:%}", "of top breeds in 2021." )
    print("The {} was".format(breed.upper()),f"{breed_per_total.iloc[1]:%}", "of top breeds in 2022." )
    print("The {} was".format(breed.upper()),f"{breed_per_total.iloc[2]:%}", "of top breeds in 2023." )
    print("The {} was".format(breed.upper()), f"{data_total_reg/data['Total'].sum():%}", "of top breeds across all years.")
    print("Most popular month(s) for {} registrations: {}".format(breed.upper(), ', '.join(popular_months.index)))

if __name__ == '__main__':
    main()
