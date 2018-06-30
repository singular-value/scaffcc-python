"""
Module for interfacing with ScaffCC compilation from Python to generate OpenQASM.

Usage:
    from scaffcc_interface import ScaffCC
    scaffold_code = "// your scaffold code goes here"
    scaffcc = ScaffCC(scaffold_code)  # can optionally pass a scaffold_path kwarg
                                      # default is '../ScaffCC/scaffold.sh'
    openqasm = scaffcc.get_openqasm()

"""

import subprocess
import sys

if sys.version_info < (3,5):
    raise Exception('Python version 3.5 or greater is needed for subprocess module usage.')


class ScaffCC():
    scaffold_filename = 'tmp.scaffold'
    openqasm_filename = 'tmp.qasm'

    def __init__(self, scaffold_code, scaffold_path='../ScaffCC/scaffold.sh'):
        self.scaffold_code = scaffold_code
        self.scaffold_path = scaffold_path
        assert subprocess.run(['test', '-f', self.scaffold_path]).returncode == 0, \
            'Could not run ./%s (did you provide path correctly?)' % self.scaffcc_path

    def get_openqasm(self):
        self._write_scaffold_file()
        subprocess.run(['bash', self.scaffold_path, '-b', self.scaffold_filename])
        openqasm = self._get_openqasm()
        self._cleanup()
        return openqasm

    def _write_scaffold_file(self):
        with open(self.scaffold_filename, 'w') as outfile:
            outfile.write(self.scaffold_code)

    def _get_openqasm(self):
        with open(self.openqasm_filename, 'r') as infile:
            return infile.read()

    def _cleanup(self):
        subprocess.run(['rm', self.scaffold_filename, self.openqasm_filename])
