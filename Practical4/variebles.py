a=15 # The walk to the bus stop is 15 mins. 
b=75 # The bus journey takes 1 hr and 15 mins.
c=a+b # The total time taken by bus is 90 mins.
d=90 # The drive takes 1 hr and 30 mins.
e=5 # The walk from the car park takes 5 mins.
f=d+e # The total time taken by car is 95 mins.
if c < f: # Compare c to e, and describe which method of commuting is quicker.
    print("c<f, The bus transport method is quicker.") # The bus is quicker.
elif c == f: # Compare c to e, and describe which method of commuting is quicker.
    print("c=f, The bus and car transport methods take the same time.") # The bus and car take the same time.
else: # Compare e to c, and describe which method of commuting is quicker.
    print("f<c, The car transport method is quicker.") # The car is quicker.

# Initialize boolean variables.
X = True
Y = False
# Create W as the logical AND of X and Y.
W = X and Y 
#   X     | Y     | W
#   True  | True  | True
#   True  | False | False
#   False | True  | False
#   False | False | False 
print(W) # This will print False.
