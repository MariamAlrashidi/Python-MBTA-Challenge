lines = {
    "Red": [
        'South Station',
        'Park Street', 'Kendall', 'Central', 'Harvard', 'Porter', 'Davis', 'Alewife'
    ],
    "Green": [
        'Government Center',
        'Park Street', 'Boylston', 'Arlington', 'Copley', 'Hynes', 'Kenmore'
    ],
    "Orange": [
        'North Station',
        'Haymarket', 'Patk Street', 'State', 'Downtown Crossing', 'Chinatown', 'Back Bay', 'Forest Hills'
    ],
}

def stopsBetweenStations(StartLine, StartStation, EndLine, EndStation):
    startStep = lines[StartLine].index(StartStation)
    endStep = lines[EndLine].index(EndStation)
    if StartLine == EndLine:
        return countingDistance(startStep, endStep), " Stops"
    else:
        startParkStep = lines[StartLine].index("Park Street")
        endParkStep = lines[EndLine].index("Park Street")
        return countingDistance(startStep, startParkStep) + countingDistance(endStep, endParkStep), " Stops"

def countingDistance(firstIndex, secondIndex):
    return abs(firstIndex - secondIndex)
print(stopsBetweenStations("Red", "Alewife", "Red", "Alewife"))
print(stopsBetweenStations("Red", "Alewife", "Red", "South Station"))
print(stopsBetweenStations("Red", "South Station", "Green", "Kenmore"))
print(stopsBetweenStations("Green", "Government Center", "Orange", "Forest Hills"))
print(stopsBetweenStations("Orange", "North Station", "Red", "Davis"))