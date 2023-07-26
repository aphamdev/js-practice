def monty(swaps):
    places = ["", "Q", ""]
    for swap in swaps:
        if swap == "L":
            places[0], places[1] = places[1], places[0]
        elif swap == "R":
            places[1], places[2] = places[2], places[1]
        else:
            places[0], places[2] = places[2], places[0]
    if places[0] == "Q":
        return "left"
    elif places[1] == "Q":
        return "middle"
    else:
        return "right"


print(monty("LRORRLOLLLRROOLRORRLOLLLRROOLRORRLOLLLRROOL"))
