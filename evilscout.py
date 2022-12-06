# A PoC implementation of the EvilScout detection algorithm.
from scapy.all import *

a = sniff(count=10)

print(a.summary())