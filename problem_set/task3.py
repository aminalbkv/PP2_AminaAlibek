# Here is a function that finds chickens and rabbits
def solve(numheads, numlegs):

    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits

        if chickens * 2 + rabbits * 4 == numlegs:
            return chickens, rabbits


# Here is the result
chickens, rabbits = solve(35, 94)

print("Chickens:", chickens)
print("Rabbits:", rabbits)