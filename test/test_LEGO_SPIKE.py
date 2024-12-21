#
# test code for Huskylens code (Python on LEGO SPIKE Version)
# V1.1
#  
#

# Revision History 
# Date Author Description 
# 2024-12-DD V1.0 Initial creation 
# 2024-12-22 V1.1 Added LINE_TRACKING  test


import time
from hub import port

# set library load path
import sys
sys.path.append('/projects/mylib000')

#
# setup UART (using port F)
#
port.F.mode(port.MODE_FULL_DUPLEX)
time.sleep(1)                   # need delay for Port setup ??
port.F.baud(9600)

#
# setup Huskylens
#
from huskylens_lib import HuskyLens
husky = HuskyLens(port.F)

from huskylens_lib import Algo

while True:

    #
    # Set the recognition alogorythm type to COLOR RECOGNITION
    #
    husky.send_CMD_REQ_ALGO(Algo.COLOR_RECOGNITION)

    #
    # read loop
    #
    for _ in range(100):
        print(husky.read_blocks())

    #
    # Set the recognition alogorythm type to LINE TRACKING
    #
    husky.send_CMD_REQ_ALGO(Algo.LINE_TRACKING)
    #
    # read loop
    #
    for _ in range(100):
        print(husky.read_arrows())




#
#
#