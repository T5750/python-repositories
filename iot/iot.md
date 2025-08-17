# IoT

## OPC-UA
OPC统一架构（UA）将各个OPC Classic规范的所有功能集成到一个可扩展的框架中，独立于平台并且面向服务

### Python OPC-UA
Python OPC UA is deprecated
- [opcua-server-minimal.py](opcua-server-minimal.py)
- [opcua-client-minimal.py](opcua-client-minimal.py)

#### Installation
```sh
pip install opcua
```

## Pymodbus
Pymodbus is a full Modbus protocol implementation offering a client and server with synchronous/asynchronous API and simulators.

| 数据区块           | 数据类型         | 访问类型 |
|--------------------|------------------|----------|
| 线圈(Coils)        | 布尔             | 读/写    |
| 离散量输入(Discrete Input) | 布尔       | 只读     |
| 输入寄存器(Input registers) | 无符号2字节整型 | 只读     |
| 保持寄存器(Holding registers) | 无符号2字节整型 | 读/写    |

### Contents
- [modbus_server.py](modbus_server.py)
- [modbus_client.py](modbus_client.py)

### Client protocols/framers
| protocol       | ASCII | RTU  | RTU_OVER_TCP | SOCKET | TLS  |
|----------------|-------|------|--------------|--------|------|
| SERIAL (RS-485) | Yes   | Yes  | No           | No     | No   |
| TCP            | Yes   | No   | Yes          | Yes    | No   |
| TLS            | No    | No   | No           | No     | Yes  |
| UDP            | Yes   | No   | Yes          | Yes    | No   |

### Installation
```sh
pip install -U pymodbus
```

## Runtime Environment
- [opcua 0.98.x](https://pypi.org/project/opcua/)
- [pymodbus 3.10.x](https://pypi.org/project/pymodbus/)

## References
- [OPC统一架构](https://www.opcfoundation.cn/about/opc-technologies/opc-ua)
- [Python OPC-UA GitHub](https://github.com/FreeOpcUa/python-opcua)
- [Python OPC-UA Documentation](https://python-opcua.readthedocs.io/en/latest/index.html)
- [Python OPC-UA Examples](https://github.com/FreeOpcUa/python-opcua/tree/master/examples)
- [OPC-UA GUI Client](https://github.com/FreeOpcUa/opcua-client-gui)
- [Pymodbus GitHub](https://github.com/pymodbus-dev/pymodbus)
- [Pymodbus Client](https://pymodbus.readthedocs.io/en/latest/source/client.html)
- [Pymodbus Examples](https://pymodbus.readthedocs.io/en/latest/source/examples.html)
- [Pymodbus Architecture](https://pymodbus.readthedocs.io/en/latest/source/library/architecture/architecture.html)