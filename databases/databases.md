# Databases

## Oracle
### python-oracledb
The python-oracledb driver is a Python programming language extension module allowing Python programs to connect to Oracle Database. Python-oracledb is the successor to the now obsolete cx_Oracle driver.

#### Installation
```sh
python -m pip install oracledb
```

#### Dependencies and Interoperability
- **Thin mode**: Oracle Database 12.1 (or later) is required
- **Thick mode**: Oracle Database 9.2 (or later) is required

#### Architecture
![](https://oracle.github.io/python-oracledb/python-oracledb-arch.jpg)

#### Samples
Examples can be found in the [/samples](https://github.com/oracle/python-oracledb/tree/main/samples) directory and the [Python and Oracle Database Tutorial](https://oracle.github.io/python-oracledb/samples/tutorial/Python-and-Oracle-Database-The-New-Wave-of-Scripting.html).

### cx_Oracle
cx_Oracle was obsoleted by python-oracledb in 2022.

#### Installation
```sh
pip install cx_Oracle
```

## Weaviate
### Installation
```sh
pip install -U weaviate-client
```

## References
- [Python python-oracledb Driver](https://oracle.github.io/python-oracledb/)
- [python-oracledb GitHub](https://github.com/oracle/python-oracledb)
- [Python and Oracle Database Tutorial](https://oracle.github.io/python-oracledb/samples/tutorial/Python-and-Oracle-Database-The-New-Wave-of-Scripting.html)
- [Python cx_Oracle](https://oracle.github.io/python-cx_Oracle/)
- [Weaviate Python](https://weaviate.io/developers/weaviate/client-libraries/python)