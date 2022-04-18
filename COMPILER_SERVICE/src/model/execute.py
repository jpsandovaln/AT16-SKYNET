import subprocess
class Execute:
    def run(self, command):
        return subprocess.check_output(command, shell=True)
