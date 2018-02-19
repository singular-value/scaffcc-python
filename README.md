# scaffcc-python

Module for interfacing with ScaffCC compilation from Python to generate OpenQASM.

Usage:
```
    from scaffcc_interface import ScaffCC
    scaffold_code = "// your scaffold code goes here"
    scaffcc = ScaffCC(scaffold_code)  # can optionally pass a scaffold_path kwarg
                                      # default is '../ScaffCC/scaffold.sh'
    openqasm = scaffcc.get_openqasm()
```
