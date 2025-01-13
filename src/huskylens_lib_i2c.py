#
# driver for HuskyLens(serial/i2c)
#
# reference
# https://github.com/HuskyLens/HUSKYLENSArduino/blob/master/HUSKYLENS%20Protocol.md

import time

DEVICE_ADDR = 0x32

from machine import Pin, I2C
i2c = I2C(0, scl=Pin(7), sda=Pin(6), freq=100000)

# >>> hex(i2c.scan()[0])
# '0x32'

class HuskyLens:

    def __init__(self, i2c=None, serial=None):
        self.algorithm = None
        if i2c is not None:
            self.i2c = i2c
            self.serial = None
        elif serial is not None:
            self.serial = serial
            self.i2c = None
        else:
            print("Error!, specifi i2c or serial")
            return None

    def get_current_algorithm(self):
        return self.algorithm

    def set_algorithm(self, algorithm):
    
        # if eqauls to current algorithm, skip
        if self.algorithm == algorithm:
              return True

        # base cmd_set: OBJECT_TRACKING
        cmd_set = bytearray((0x55, 0xAA, 0x11, 0x02, 0x2D, 0x01, 0x00, 0x40))
    
        algo = None
        if algorithm == 'FACE_RECOGNITION':
            algo = (0x00,0x00)
        elif  algorithm == 'OBJECT_TRACKING':
            algo = (0x01,0x00)
        elif  algorithm == 'OBJECT_RECOGNITION':
            algo = (0x02,0x00)
        elif  algorithm == 'LINE_TRACKING':
            algo = (0x03,0x00)
        elif  algorithm == 'COLOR_RECOGNITION':
            algo = (0x04,0x00)
        elif  algorithm == 'TAG_RECOGNITION':
            algo = (0x05,0x00)
        elif  algorithm == 'OBJECT_CLASSIFICATION':
            algo = (0x06,0x00)
        else:
            print("internal Error in set_algorithm")
            print(f"unk algorithm type {algorithm}")
            return None
    
        if algo:
            cmd_set[5] = algo[0]
            cmd_set[6] = algo[1]
            cmd_set[7] = make_chksum(cmd_set[0:7])
            #print([hex(x) for x in cmd_set])
            self.send_data(cmd_set)
    
            # read ret_ok or not
            buf = bytearray(6)
            for _ in range(5):
                print('get ret ok')
                status = self.receive_cmd_ret_ok(buf)
                if status is True:
                        break
                else:
                        time.sleep(0.1)
        return status
    
    #
    #  id,x_center,y_center,width,height
    #
    
    def get_blocks(self):
        buf = bytearray(16)
        self.send_cmd_req_blocks()
        flag = self.receive_cmd_return_info(buf)
        blocks = []
        if flag:
            n_of_blocks=buf[5] +  (buf[6]<<8)
            for _ in range(n_of_blocks):
                value = self.receive_cmd_return_block(buf)
                if value:
                    blocks.append(value)
        print(blocks)
        return blocks
    
    #
    #  ID, x_org,y_org,x_target,y_target
    #
    def get_arrows(self):
        buf = bytearray(16)
        self.send_cmd_req_arrows()
        flag = self.receive_cmd_return_info(buf)
        arrows = []
        if flag:
            n_of_arrows=buf[5] +  (buf[6]<<8)
            print(f"N of Arrows: {n_of_arrows}")
            for _ in range(n_of_arrows):
                value = self.receive_cmd_return_arrow(buf)
                if value:
                   arrows.append(value)
        print(arrows)
        return arrows
    
    def send_cmd_req_knock(self):
        self.send_data(bytes((0x55, 0xAA, 0x11, 0x00, 0x2C, 0x3C)))
    
    def send_cmd_req_algo(self):
        self.send_data(bytes((0x55, 0xAA, 0x11, 0x02, 0x2D, 0x01, 0x00, 0x40)))
    
    def send_cmd_req_blocks(self, learned=True):
        if learned:
            # COMMAND_REQUEST_BLOCKS_LEARNED (0x24):
            self.i2c.writeto(DEVICE_ADDR, bytes((0x55, 0xAA, 0x11, 0x00, 0x24, 0x34)))
        else:
            # COMMAND_REQUEST_BLOCKS (0x21):
            self.i2c.writeto(DEVICE_ADDR, bytes((0x55, 0xAA, 0x11, 0x00, 0x21, 0x31)))
    
    def send_cmd_req_arrows(self, learned=True):
        if learned:
            # COMMAND_REQUEST_ARROWS_LEARNED (0x25):
            self.i2c.writeto(DEVICE_ADDR, bytes((0x55, 0xAA, 0x11, 0x00, 0x25, 0x35)))
        else:
            # COMMAND_REQUEST_ARROWS (0x22):
            self.i2c.writeto(DEVICE_ADDR, bytes((0x55, 0xAA, 0x11, 0x00, 0x22, 0x32)))
    
    def receive_cmd_ret_ok(self, buf):
        self.receive_data(buf)
        if buf[0] == 0x55 and buf[4] == 0x2E:
             return True
        else:
             return False
    
    def receive_cmd_return_info(self, buf):
        self.receive_data(buf)
        if buf[0] == 0x55 and buf[4] == 0x29:
             return True
        else:
             return False
    
    def receive_cmd_return_block(self, buf):
        self.receive_data(buf)
        if buf[0] == 0x55 and buf[4] == 0x2A:
             print([hex(x) for x in buf[5:15]])
             x_center = (buf[6]<<8) + buf[5]
             y_center = (buf[8]<<8) + buf[7]
             width = (buf[10]<<8) + buf[9]
             height = (buf[12]<<8) + buf[11]
             id = (buf[14]<<8) + buf[13]
             return (id,x_center,y_center,width,height)
        else:
             return False
    
    def receive_cmd_return_arrow(self, buf):
        self.receive_data(buf)
        if buf[0] == 0x55 and buf[4] == 0x2B:
             print([hex(x) for x in buf[5:15]])
             x_origin = (buf[6]<<8) + buf[5]
             y_origin = (buf[8]<<8) + buf[7]
             x_target = (buf[10]<<8) + buf[9]
             y_target = (buf[12]<<8) + buf[11]
             id = (buf[14]<<8) + buf[13]
             return (id,x_origin,y_origin,x_target,y_target)
        else:
             return False
    
    def make_chksum(self, buf):
        return (sum(buf) & 0xff)
    
    def send_data(self, cmd):
        self.i2c.writeto(DEVICE_ADDR, cmd)
    
    def receive_data(self, buf):
        self.i2c.readfrom_into(DEVICE_ADDR, buf, True)
    
    
