from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusDeviceContext,
)
from pymodbus.server.startstop import (
    StartTcpServer,
)

dataBlock = ModbusSequentialDataBlock.create()
context = ModbusDeviceContext(
    di=dataBlock,
    co=dataBlock,
    hr=dataBlock,
    ir=dataBlock,
)
single = True

# Build data storage
store = ModbusServerContext(devices=context, single=single)

if __name__ == '__main__':
    address = ("0.0.0.0", 502)
    StartTcpServer(
        context=store,  # Data storage
        address=address,  # listen address
    )
