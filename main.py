BASE_FLIGHT_COST_AMS = 150.00
BASE_FLIGHT_COST_GLA = 80.00

def main():
    flightSpecification = input("Enter flight specification: ")

    destination = flightSpecification[0:3]
    numberOfBags = int(flightSpecification[4])
    passengerAge = int(flightSpecification[6:8])
    mealType = flightSpecification[9]
    seatingClass = flightSpecification[11]

    if destination == "AMS":
        destinationAirport = "Schiphol, Amsterdam"
        flightCost = BASE_FLIGHT_COST_AMS
    elif destination == "GLA":
        destinationAirport = "Glasgow, Scotland"
        flightCost = BASE_FLIGHT_COST_GLA
    else:
        print("Invalid destination.")
        return

    # Calculate the baggage cost
    if numberOfBags > 1:
        baggageCost = (numberOfBags - 1) * 20
    else:
        baggageCost = 0

    # Check if the passenger is a child
    if passengerAge <= 15:
        flightCost /= 2
        passengerType = "Child"
    else:
        passengerType = "Adult"

    # Calculate the meal cost
    if mealType == "S":
        mealCost = 10.00
        mealTypeName = "Standard Meal"
    elif mealType == "V":
        mealCost = 12.00
        mealTypeName = "Vegetarian Meal"
    else:
        mealCost = 0
        mealTypeName = "No Meal"

    #discount meal cost for a child passenger
    if passengerAge <= 15:
        mealCost -= 2.50

    # Calculate the seating class and adjust the flight cost accordingly
    if seatingClass == "E":
        seatingClassName = "Economy Class"
    elif seatingClass == "F":
        seatingClassName = "First Class"
        flightCost *= 6
        mealCost = 0

    # Calculate the total cost
    totalCost = flightCost + baggageCost + mealCost

    # Output a summary of the specified flight along with the costs involved
    print(f"Flight to {destinationAirport}:\n"\
          f"Flight cost: £{flightCost}\n"\
          f"Number of bags: {numberOfBags}\n"\
          f"Baggage cost: £{baggageCost}\n"\
          f"Passenger type: {passengerType}\n"\
          f"Meal type: {mealTypeName}\n"\
          f"Meal cost: £{mealCost}\n"\
          f"Seating class: {seatingClassName}\n"\
          f"Total cost: £{totalCost}")

if __name__ == "__main__":
    main()
