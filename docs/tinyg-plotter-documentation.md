Notes
=====
* In order to open port on lubuntu need to add user to dialout:
  * groups
  * sudo adduser wojcikpwl dialout


* CuteCom used as terminal, connection details:
  * Device: /dev/ttyS0
  * Baud rate: 115200
  * Handshake: Hardware (CTS/RTS) need to be configured on tinyG $ex
  * example: ser = serial.Serial(port="/dev/cu.usbserial-DN00WNBE",baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1, xonxoff=False, rtscts=True, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)


  * Homing gcode:
    * G28.2X0Y0
