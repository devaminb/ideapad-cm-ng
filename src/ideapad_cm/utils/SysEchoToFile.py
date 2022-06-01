from ideapad_cm.utils.SysRunner import SysRunner


class SysEchoToFile(SysRunner):
    def __init__(self, content: str, file: str, append: bool = False):
        # TODO: Validate content and file
        super().__init__()
        if append:
            operator = ">>"
        else:
            operator = ">"
        self.command = ["echo", content, operator, file]
