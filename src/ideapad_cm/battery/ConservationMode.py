from ideapad_cm.battery.CantReadStatusError import CantReadStatusError
from ideapad_cm.utils.SysEchoToFile import SysEchoToFile


class ConservationMode:
    def __init__(self):
        # TODO: Check if the module ideapad_acpi exists and is loaded
        self.__ideapad_acpi_path = \
            "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"

    def enable(self):
        SysEchoToFile("1", self.__ideapad_acpi_path).sudo_run()

    def disable(self):
        SysEchoToFile("0", self.__ideapad_acpi_path).sudo_run()

    def status(self):
        with open(self.__ideapad_acpi_path, "r") as file:
            returned_status = file.read().replace("\n", "")

        if returned_status == "1":
            return True
        elif returned_status == "0":
            return False
        else:
            raise CantReadStatusError()
