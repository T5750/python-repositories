from pymodbus.client import ModbusTcpClient
from pymodbus.pdu.bit_message import ReadCoilsResponse
from pymodbus.pdu.register_message import ReadInputRegistersResponse

host = '127.0.0.1'
port = 502
client = ModbusTcpClient(host, port=port)

# 写入线圈
client.write_coil(1, True)
client.write_coil(2, False)
client.write_coil(3, True)

# 读取线圈，注意对于离散量的读取，第二个参数count是有坑的，必须为8的倍数个
result: ReadCoilsResponse = client.read_coils(address=1, count=8)  # 从地址1开始读，读取8个线圈，一次读8的倍数个线圈，不设置为8的倍数可能会出现问题
print('result.isError:', result.isError())
print('read_coils:', result.bits)  # 打印读取结果，一共8位
# 读取其中的位
print(
    result.bits[0],
    result.bits[1],
    result.bits[2]
)

# 读取离散量输入
result = client.read_discrete_inputs(address=10001, count=8)  # 从10001开始读，读取8位
print('read_discrete_inputs:', result.bits)

# 读取输入寄存器
input_register_result: ReadInputRegistersResponse = client.read_input_registers(1, count=8)
print('read_input_registers:', input_register_result.registers)

# 读写保持寄存器
client.write_register(address=40001, value=100)
result: ReadInputRegistersResponse = client.read_holding_registers(address=40001, count=1)
print('read_holding_registers:', result.registers)

# 关闭连接
client.close()
