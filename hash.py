from hashids import Hashids
import random


def key():
    hashids = Hashids(salt="asdkfhioahr89234123412;34'1234dx.1;23.41234d[1234c]2;3]4.qw.;r'.wqe';.rqw]e[r;")
    id = hashids.encode(random.randint(0,100000000000), random.randint(0,100000000000), random.randint(0,100000000000))
    return id
