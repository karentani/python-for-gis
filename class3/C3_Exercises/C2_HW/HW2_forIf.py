# Leave this alone!
animal_list = ['zebra', 'kitty', 'puppy', 'lizard', 'kitty', 'kitty',
               'hedgehog', 'fish', 'puppy', 'giraffe', 'sloth',
               'lion', 'puppy', 'bunny', 'tiger', 'platypus', 'puppy']

"""
Write your code below:
1. Define a variable called puppy_counter and set it equal to 0
2. Use for to loop through every animal in animal_list
3. If the animal is a puppy, increase puppy_counter by 1
4. Once the for loop is complete, print the total number of puppies
"""

puppy_counter = 0

for animal in animal_list:

    if animal == 'puppy':
        puppy_counter += 1

print 'The total number of puppies equals ' + str(puppy_counter)

# Then count kitties... Then change puppy to 'corgi'
