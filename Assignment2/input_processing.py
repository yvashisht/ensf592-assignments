# input_processing.py
# Yajur Vashisht ENSF 592 P23
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self, light = 'green', pedestrian = 'no', vehicle = 'no'):
        self.light = light #attribute light which is used for what colour the traffic light is
        self.pedestrian = pedestrian #attribute pedestrian which is used for whether a pedestrian is present or not
        self.vehicle = vehicle #attribute vehicle which is used for whether a vehicle is present or not
        pass

    def update_status(self): 
        
        print("Are changes detected in the vision input? ") #prints the initial line

        try:
            change = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ") #change asks for the initial change from the default settings

            if change not in ["0", "1", "2", "3"]:
                raise ValueError
            else: 
                if change == "1": #evalutes the following code when the user inputs 1 
                    input_1 = input("What change has been identified?: ")
                    if input_1 in ["green", "yellow", "red"]: #ensures the input is one we were expecting
                        self.light = input_1
                    else: 
                        print("Invalid vision change \n") #lets the user know the input is not allowed 
                elif change == "2": #evalutes the following code when the user inputs 2
                    input_2 = input("What change has been identified?: ")
                    if input_2 in ["yes", "no"]: #ensures the input is one we were expecting
                        self.pedestrian = input_2
                    else:
                        print("Invalid vision change \n") #lets the user know the input is not allowed 
                elif change == "3": #evalutes the following code when the user inputs 3
                    input_3 = input("What change has been identified?: ")
                    if input_3 in ["yes", "no"]: #ensures the input is one we were expecting
                        self.vehicle = input_3
                    else:
                        print("Invalid vision change \n") #lets the user know the input is not allowed 
                elif change == "0":
                    print("\n")
        except ValueError:
            print("You must select either 0, 1, 2, 3") 
            return "null"
        return change

# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes": #prints stop if the conditions are as set 
        print ("\n STOP \n")
    if sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no": #prints caution if the conditions are as set 
        print ("\n Caution \n")
    if sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no": #prints proceed if the conditions are as set 
        print ("\n Proceed \n")
    pass

# Complete the main function below
def main():
    print("\n***ENSF 592 Car Vision Detector Processing Program***\n")

    vehicle_sensor = Sensor() #makes an object of the class Sensor
    user_entry = " " #initially sets user_entry

    while True:
        user_entry = vehicle_sensor.update_status() #if true then the user_entry is updated to vehicle_sensor object with method update_status()
        if user_entry == "0":
            break #breaks the program if the user enters 0
        elif user_entry != "null":
            print_message(vehicle_sensor) #prints the vehicle_sensor object 
            print("Light = " + vehicle_sensor.light + "," + " Pedestrian = " + 
              vehicle_sensor.pedestrian + "," + " Vehicle = " + vehicle_sensor.vehicle +"\n") #prints the updated status
            
if __name__ == '__main__':
    main()