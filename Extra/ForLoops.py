# For loops in python

"""

For loops will execute a block of code a fixed number of times

You can iterate over a range, a string, sequence. etc


"""

# to count to 10
for x in range(1,11, 2): # we can add an extra comma to say the way well be counting
# whatever code will be repeated will be here
    print(x)
print("GET OUT OF THE LOOP")

for y in reversed(range(1,11)): # this will make it count backwards
    print(y)

## to skip a character use the continue function

for pix in range(1,21): # it skips 13
    if pix == 13:
        continue # if we use break it will stop entirely the code
    else:
        print(pix)