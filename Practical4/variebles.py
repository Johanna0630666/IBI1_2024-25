c=0
a=15
b=60+15
c=a+b
d=60+30
e=5
f=d+e
if c>=f :                               #compare c and f
    print("f is quicker than c")
else:
    print("c is quicker than f")        #That's the answer.



X = True
Y = False
W = X and Y

# Truth table for W:
# X     Y     W
# True  True  True
# True  False False
# False True  False
# False False False

print(W) #The table shows that W is True only when both X and Y are True. In all other cases, W is False.