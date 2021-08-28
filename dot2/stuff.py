from pathlib import Path
from typing import Sequence, Union

PathTypes = Union[Path, str]


class OsFileWrite:
    def __init__(self, filename: PathTypes, nl: bytes):
        self.filename = filename
        self.nl = nl
        self.f_obj = None

    def open(self):
        self.f_obj = open(self.filename, "wb")

    def close(self):
        self.f_obj.close()

    def write(self, bts: bytes):
        self.f_obj.write(bts)

    def write_line(self, ln: str):
        self.write(ln.encode())
        self.write(self.nl)

    def write_line_seq(self, lines: Sequence[str]):
        for ln in lines:
            self.write_line(ln)


class UnixFileWrite(OsFileWrite):
    def __init__(self, filename: PathTypes):
        super(UnixFileWrite, self).__init__(filename, b"\n")


class WindowsFileWrite(OsFileWrite):
    def __init__(self, filename: PathTypes):
        super(WindowsFileWrite, self).__init__(filename, b"\r\n")
