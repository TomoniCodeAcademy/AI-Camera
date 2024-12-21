#
# test code for Huskylens code (Python on LEGO SPIKE Version)
#

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

#
# Set the recognition alogorythm type for the AI camera."
#
from huskylens_lib import Algo
husky.send_CMD_REQ_ALGO(Algo.COLOR_RECOGNITION)

#
# read loop
#
while True:
    print(husky.read_blocks())


#
#
#