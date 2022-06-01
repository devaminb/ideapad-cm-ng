import subprocess
from abc import ABC


class SysRunner(ABC):
    def __init__(self):
        self.command = None

    @staticmethod
    def __run(command: list):
        return_code = subprocess.call(command)
        return return_code

    def user_run(self):
        return_code = self.__run(self.command)
        return return_code

    def sudo_run(self):
        command = self.command.copy()
        command_str = " ".join(command)
        sh_command = ["sh", "-c", command_str]
        sh_command.insert(0, "/usr/bin/sudo")
        return_code = self.__run(sh_command)
        return return_code
