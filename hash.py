from hashids import Hashids
import random

salt = "asdkfoajsdf@%$#%@#@#kdalf;[asdf.as,dfdsaf!@#%$#&*$%"

def key():
    hashids = Hashids(salt=salt)
    id = hashids.encode(random.randint(0,100000000000), random.randint(0,100000000000), random.randint(0,100000000000))
    return id
