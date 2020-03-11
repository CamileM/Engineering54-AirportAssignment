from aircraft_class import *
from plane_class import *
from people_class import *
from passenger_class import *
from flight_trip_class import *

user_input = ''

list_of_passenger = []


print('')
print(30 * '=', 'AIRPORT MAIN MENU', 30 * '=')

user_input = print("1. To Create A Plane")
user_input = print("2. To Create A Passenger")
user_input = print("3. To Create A Flight Trip")
user_input = print("4. Press 'x' To Exit The Program")
print('')
print(25 * '=', "CHOOSE A NUMBER FROM [1 - 3]", 25 * '=')

while True:

    if user_input == '1':

        print(30 * '=', "ADDING A PLANE", 30 * '=')
        name_of_plane = input("Enter The Name Of The Plane: \n")
        plane = Plane(plane_number)

        # print('')
        # user_input = input("If You Want To Quit The Program Then Press 'x' \n")
        # continue

        breakpoint()

    elif user_input == '2':

       print(30 * '=', "ADDING A PASSENGER", 30 * '=')
       first_name = input("Enter A First Name:\n")
       last_name = input("Enter A Second Name:\n")
            # print(5 * '*', "PASSPORT NUMBER", 5 * '*')

            # print('')
            # user_input = input("If You Want To Quit The Program Then Press 'x' \n")
            # continue

    elif user_input == '3':

        print(30 * '=', "CREATING A FLIGHT TRIP", 30 * '=')
        origin = print("Enter Your Current Location: \n")
        destination = print("Enter Your Next Destination: \n")
        plane_number = []

            # print('')
            # user_input = input("If You Want To Quit The Program Then Press 'x' \n")
            # continue

    elif user_input == 'x':

        print('Program Shutting Down In 3 2 1...')
        break