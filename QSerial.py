from PyQt5.Qt import *

infos = QSerialPortInfo.availablePorts()  # 查看可用端口
print(infos)
for info in infos:
    description = info.description()  # 描述
    manufacturer = info.manufacturer()  # 制造商
    serialNumber = info.serialNumber()  # 串口号

print(description)
print(manufacturer)
print(serialNumber)

