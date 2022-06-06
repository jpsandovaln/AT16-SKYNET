import subprocess
from subprocess import STDOUT, PIPE


class Executer:
    def execute(self, cmd):
        proc = subprocess.Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
        output = proc.stdout.read().decode('utf-8')
        return output
