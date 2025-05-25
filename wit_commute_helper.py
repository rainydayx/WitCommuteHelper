import time
import os 

def wit_commute_assistant():


    while True:
        print("Welcome to the WIT Commute Assistant!")
        time.sleep(0.5)
        print("Where are you right now?")
        time.sleep(0.5)
        print("A. SM City Iloilo")
        time.sleep(0.5)
        print("B. Molo Plaza")
        time.sleep(0.5)
        print("C. Jaro Plaza")
        time.sleep(0.5)
        print("D. Mandurriao Plaza")
        time.sleep(0.5)
        print("E. Lapaz Plaza")
        time.sleep(0.5)
        print("F. Exit")  

        while True:
            choice = input("Enter the letter corresponding to your location: ").upper()
            if choice in ['A', 'B', 'C', 'D', 'E', 'F']:
                break
            else:
                print("Invalid choice. Please enter a letter from A to F.")

        if choice == 'F':
            print("Thank you for using the WIT Commute Helper!")
            break

        print("\nCalculating your commute...")
        time.sleep(1)  

        if choice == 'A':
            print("From SM City Iloilo, ride the SM City Nabitasan Lapaz jeepney going towards Lapaz. ")
            time.sleep(1)
            print("Estimated Fare: ₱12-₱14")
        elif choice == 'B':
            print("From Molo Plaza, ride a Baluarte jeepney and get off at Atrium.")
            time.sleep(1)
            print("Then, ride a CPU jeepney going to WIT.")
            time.sleep(1)
            print("Estimated Total Fare: ₱25-₱30")
        elif choice == 'C':
            print("From Jaro Plaza, ride a CPU or Tagbak Terminal jeepney and get off at WIT.")
            time.sleep(1)
            print("Estimated Fare: ₱12-₱14")
        elif choice == 'D':
            print("From Mandurriao Plaza, ride a Jaro Plaza Mandurriao jeepney and get off at Jaro Plaza.")
            time.sleep(1)
            print("Then, ride a CPU jeepney and get off at Saint Clements.")
            time.sleep(1)
            print("Estimated Total Fare: ₱24-₱30")
        elif choice == 'E':
            print("From Lapaz Plaza, ride the Nabitasan Lapaz jeepney and get off at Nabitasan.")
            time.sleep(1)
            print("Estimated Fare: ₱12-₱14")

        input("\nPress Enter to check another location...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    wit_commute_assistant()