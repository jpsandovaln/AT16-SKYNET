import subprocess


class Execute:
    def run(self, command: str) -> str:
        return subprocess.check_output(command, shell=True)
