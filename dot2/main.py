from pathlib import Path

from alias import bat_generate
from aliases_defs import alias_seq


def main():
    aliases = alias_seq()
    # pathes = path_seq()
    bat_generate(aliases, Path("c:/bin/aliases"))


if __name__ == "__main__":
    main()
