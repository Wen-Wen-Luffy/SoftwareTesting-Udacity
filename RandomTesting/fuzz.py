# this is from Charlie Miller's "Babysitting an Army of Monkeys"
# comments are mine

import random
import math

# load file into buffer

numwrites = random.randrange(math.ceil(float(len(buf)) / FuzzFactor)) + 1
for j in range(numwrites):
    rbyte = random.randrange(256)
    rn = random.randrange(len(buf))
    buf[rn] = "%c" % rbyte

# save buffer

# run process

# look at exit code

# if it doesn's die, kill it

# start over