# school_data.py
# AUTHOR NAME: Yajur Vashisht

# A terminal-based application for computing and printing statistics based on given input

import numpy as np
import numpy.ma as ma
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

data = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022] #creating an array
data = np.reshape(data, (10,20,3)) #reshaping the array using numpy into the desired dimensions

#dictionary of school names corresponding to the school code

school_dic = { 

    "Centennial High School": "1224",
    "Robert Thirsk School": "1679",
    "Louise Dean School": "9626",
    "Queen Elizabeth High School": "9806",
    "Forest Lawn High School": "9813",
    "Crescent Heights High School": "9815",
    "Western Canada High School": "9816",
    "Central Memorial High School": "9823",
    "James Fowler High School": "9825",
    "Ernest Manning High School": "9826",
    "William Aberhart High School": "9829",
    "National Sport School": "9830",
    "Henry Wise Wood High School": "9836",
    "Bowness High School": "9847",
    "Lord Beaverbrook High School": "9850",
    "Jack James High School": "9856",
    "Sir Winston Churchill High School": "9857",
    "Dr. E. P. Scarlett High School": "9858",
    "John G Diefenbaker High School": "9860",
    "Lester B. Pearson High School": "9865"
}

school_names = list(school_dic.keys())
school_codes = list(school_dic.values())

def main():

    print("ENSF 592 School Enrollment Statistics")
    # Prints the Stage 1 requirements
    print("Shape of full data array: " ,data.shape)
    print("Dimensions of full data arry: " ,data.ndim)

    # Prompt for user input

    while True:

        initial_input = input("Please enter the high school name or school code: ") #receiving input from user

        try:
            if initial_input in school_dic or initial_input in school_dic.values(): #checking if it is a valid input
                break
            else: 
                raise ValueError #raises a value error if the input is not valid from the user
        except ValueError:
            print("You must enter a valid school name or code.")

    #getting the index to reference the school enrollment data based on what the user inputs

    if initial_input in school_dic:
        index = school_names.index(initial_input) 
    else:
        index = school_codes.index(initial_input)
    
    #used to print the school name and code after determining where it is in the dictionary keys and values

    if initial_input in school_dic:
            school_name = initial_input
            school_code = school_dic[initial_input]
    elif initial_input in school_dic.values():
            school_code = initial_input
            school_name = [i for i, value in school_dic.items() if value == initial_input][0]

    # Prints the Stage 2 requirements 

    print("\n***Requested School Statistics***\n")
    print("School name:",school_name,", School Code:",school_code)
    print("Mean enrollment for Grade 10: " ,(int)(np.nanmean(data[:,index,0])))
    print("Mean enrollment for Grade 11: " ,(int)(np.nanmean(data[:,index,1])))
    print("Mean enrollment for Grade 12: " ,(int)(np.nanmean(data[:,index,2])))
    print("Highest enrollment for a single grade: " ,(int)(np.nanmax(data[:,index,:])))
    print("Lowest enrollment for a single grade: " ,(int)(np.nanmin(data[:,index,:])))
    print("Total enrollment for 2013: " ,(int)(np.nansum(data[0,index,:])))
    print("Total enrollment for 2014: " ,(int)(np.nansum(data[1,index,:])))
    print("Total enrollment for 2015: " ,(int)(np.nansum(data[2,index,:])))
    print("Total enrollment for 2016: " ,(int)(np.nansum(data[3,index,:])))
    print("Total enrollment for 2017: " ,(int)(np.nansum(data[4,index,:])))
    print("Total enrollment for 2018: " ,(int)(np.nansum(data[5,index,:])))
    print("Total enrollment for 2019: " ,(int)(np.nansum(data[6,index,:])))
    print("Total enrollment for 2020: " ,(int)(np.nansum(data[7,index,:])))
    print("Total enrollment for 2021: " ,(int)(np.nansum(data[8,index,:]))) 
    print("Total enrollment for 2022: " ,(int)(np.nansum(data[9,index,:])))
    print("Total ten year enrollment: " ,(int)(np.nansum(data[:,index,:]))) 
    print("Mean total enrollment over 10 years: " ,(int)(np.nanmean(data[:,index,:])))

    #if and else statement which only prints the values provided the data is >500 
    #data_useful returns true or false depending on the inputted index

    data_useful = np.any(data[:,index,:] > 500)

    if data_useful:
        stage2_data = data[:,index,:]
        print("For all enrollments over 500, the median value was: ", (int)(np.ma.median(stage2_data)))
    else:
         print("No enrollments over 500.")

    # Prints the Stage 3 requirements

    print("\n***General Statistics for All Schools***\n")

    #removes the NaN values in the array

    data_nan = ma.masked_invalid(data)

    print("Mean enrollment in 2013: " ,(int)(np.nanmean(data_nan[0,:,:])))
    print("Mean enrollment in 2022: " ,(int)(np.nanmean(data_nan[9,:,:])))
    print("Total graduating call of 2022: " ,(int)(np.nansum(data_nan[9,:,2])))
    print("Highest enrollment for a single grade: " ,(int)(np.nanmax(data_nan[:,:,:])))
    print("Lowest enrollment in 2022: " ,(int)(np.nanmin(data_nan[:,:,:])))

if __name__ == '__main__':
    main()