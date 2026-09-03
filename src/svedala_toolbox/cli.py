"""Command line interface: `svedala info` and `svedala pf`.

The argument parsing is wired up for you. Lab 1: fill in the two command
functions using your loader module.
"""
import argparse

from . import loader


def cmd_info(args: argparse.Namespace) -> None:
    """Print what the network contains: element counts and zones.

    TODO (Lab 1): load the network and print, at minimum, the number of
    buses/lines/transformers/generators/loads and the list of zones.
    """
    raise NotImplementedError("Lab 1: implement `svedala info`")


def cmd_pf(args: argparse.Namespace) -> None:
    """Run a power flow and print a summary.

    TODO (Lab 1): load, optionally scale all loads by --scaling, run the
    power flow, and print total load, losses, the worst line loading and
    the voltage range. One decimal is plenty.
    """
    raise NotImplementedError("Lab 1: implement `svedala pf`")


# The shell finds `svedala` because pyproject.toml declares
# [project.scripts] svedala = "svedala_toolbox.cli:main". The editable
# install wrote an executable `svedala` shim into .venv/bin (Scripts\ on
# Windows), and activation put that folder first on PATH. This function
# is what the shim calls.
def main() -> None:
    parser = argparse.ArgumentParser(prog="svedala", description=__doc__)
    # required=True means argparse itself rejects a bare `svedala` and prints
    # the usage and error text — built from prog and the subcommand names;
    # the description and help= strings show up under -h. No code of ours
    # prints any of it.
    sub = parser.add_subparsers(dest="command", required=True)

    p_info = sub.add_parser("info", help="show what the Svedala model contains")
    p_info.set_defaults(func=cmd_info)

    p_pf = sub.add_parser("pf", help="run a power flow and print a summary")
    p_pf.add_argument("--scaling", type=float, default=1.0,
                      help="scale all loads by this factor (default 1.0)")
    p_pf.set_defaults(func=cmd_pf)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
