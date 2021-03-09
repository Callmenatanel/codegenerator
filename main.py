import random
import string
import sys

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(result_str)

for x in range( int(sys.argv[2]) ):
    get_random_string( int(sys.argv[1]) )

