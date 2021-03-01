import re
import sys
from typing import Dict

USAGE = (
    f"Usage: {sys.argv[0]} [-s <separator>] [first [increment]] last"
)
VER = (
    f"Version 0.0.1"
)


args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|(--(?P<VER>version).*)|
        ((?:-s|--separator)\s(?P<SEP>.*?)\s)?
        ((?P<OP1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
    )
    $
""",
    re.VERBOSE,
)


def parse(arg_line: str) -> Dict[str, str]:
    args: Dict[str, str] = {}
    if match_object := args_pattern.match(arg_line):
        args = {k: v for k, v in match_object.groupdict().items()
                if v is not None}
    return args


def main() -> None:
    args = parse(" ".join(sys.argv[1:]))
    if not args:
        raise SystemExit(USAGE)
    elif args.get("HELP"):
        print(USAGE)
        return
    elif args.get("VER"):
        print(VER)
        return

if __name__ == '__main__':
    main()
