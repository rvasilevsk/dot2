from pathlib import Path
from typing import Sequence

from dot2.stuff import PathTypes, WindowsFileWrite

TARGET_BASH, TARGET_BAT, TARGET_DOSKEY = range(3)


class Alias:
    def __init__(
        self, name, body, default_args=None, targets=None, tags=None, echo_flag=False
    ):
        self.name = name
        self.body = body
        self.default_args = default_args
        self.targets = targets
        self.tags = tags
        self.echo_flag = echo_flag

    def is_target(self, target):
        if self.targets is None:
            return True
        return target in self.targets

    def bat_sign_at(self):
        return "" if self.echo_flag else "@"

    def bat_write(self, root_path: PathTypes):
        file_path = Path(root_path) / f"{self.name}.bat"
        f = WindowsFileWrite(file_path)
        f.open()
        f.write_line_seq(self.as_bat_lines())
        f.close()

    def as_bat_lines(self):
        body = f"{self.bat_sign_at()}{self.body} %*"
        yield body


def bat_generate(aliases: Sequence[Alias], root_path: PathTypes):
    for alias in aliases:
        if alias.is_target(TARGET_BAT):
            alias.bat_write(root_path)
            # file_path = root_path / f"{alias.name}.bat"
            # content = "\n".join(alias.as_bat_lines())
            # print(file_path)
            # print(content)
            # print("-----------------------")
