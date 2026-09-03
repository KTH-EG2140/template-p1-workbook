#!/usr/bin/env python3
"""Lab 1 self-check. Run from the repo root:  python checks/lab1_check.py

Tells you which Lab 1 goals are met. Green on everything = done.
This is a self-check for your own benefit — not a hand-in.
"""
import importlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Work from the repo root no matter where the script was started.
os.chdir(Path(__file__).resolve().parents[1])

OK, FAIL = "\033[92mPASS\033[0m", "\033[91mFAIL\033[0m"
results = []


def check(name, fn):
    try:
        fn()
        results.append((name, True, ""))
        print(f"  {OK}  {name}")
    except Exception as e:
        results.append((name, False, str(e)))
        print(f"  {FAIL}  {name}  ->  {type(e).__name__}: {e}")


def c1_installed():
    importlib.import_module("svedala_toolbox")


def c2_loader():
    from svedala_toolbox.loader import load_svedala
    net = load_svedala()
    assert len(net.bus) == 52, f"expected 52 buses, got {len(net.bus)}"
    assert net.line.max_i_ka.notna().all(), "some lines still lack a current limit"
    # Not just "filled" — filled with the RIGHT values, per voltage level.
    limits = set(net.line.max_i_ka.round(3))
    assert limits == {0.9, 1.0, 2.0}, (
        f"line limits should be exactly the DEFAULT_I_KA values 0.9/1.0/2.0 kA, got {sorted(limits)}")
    # Spot-check one named line: CL5 runs at 400 kV, so its limit must be 2.0 kA.
    cl5 = net.line.loc[net.line.name == "CL5", "max_i_ka"]
    assert len(cl5) == 1 and abs(cl5.iloc[0] - 2.0) < 1e-6, (
        "line CL5 is a 400 kV line — its limit should be 2.0 kA (check your voltage lookup)")
    # The slack flag from generators.csv must survive into the network.
    slack_names = list(net.gen.loc[net.gen.slack, "name"])
    assert slack_names == ["HÄLLAN_G1"], (
        f"expected exactly one slack generator, HÄLLAN_G1, got {slack_names}")


def c3_power_flow():
    from svedala_toolbox.loader import load_svedala, run_power_flow
    net = run_power_flow(load_svedala())
    assert net.converged
    assert abs(net.res_load.p_mw.sum() - 10981) < 10, "unexpected total load"
    # Reactive power matters too — catches a loader that drops the q_mvar column.
    assert abs(net.res_load.q_mvar.sum() - 3348) < 40, (
        "unexpected total reactive load — did q_mvar make it from loads.csv into the network?")


def _last_line(text: str) -> str:
    """The final line of a traceback is the error itself — show that, not a cut-off tail."""
    lines = text.strip().splitlines()
    return lines[-1] if lines else "(no error output)"


def c4_cli():
    exe = str(Path(sys.executable).with_name("svedala"))
    if not Path(exe).exists():
        exe = shutil.which("svedala")
    assert exe, "the `svedala` command was not found — is the package installed with `pip install -e .`?"
    out = subprocess.run([exe, "info"], capture_output=True, text=True, timeout=120)
    assert out.returncode == 0, _last_line(out.stderr)
    assert "52" in out.stdout, "`svedala info` should mention the 52 buses"
    out = subprocess.run([exe, "pf"], capture_output=True, text=True, timeout=300)
    assert out.returncode == 0, _last_line(out.stderr)


def c5_tests():
    out = subprocess.run([sys.executable, "-m", "pytest", "-q", "tests"],
                         capture_output=True, text=True, timeout=600)
    assert out.returncode == 0, out.stdout[-300:]
    # the model test file ships with 2 tests + smoke; "your test" makes it >= 4
    tail = out.stdout.strip().splitlines()[-1]
    import re
    m = re.search(r"(\d+) passed", tail)
    assert m, tail
    assert int(m.group(1)) >= 4, (
        f"only {m.group(1)} tests pass — did you write your own test in tests/test_loader.py?")


print("Lab 1 self-check")
check("package installed (pip install -e .)", c1_installed)
check("loader builds the network, limits filled", c2_loader)
check("power flow runs and converges", c3_power_flow)
check("CLI works: svedala info / svedala pf", c4_cli)
check("test suite green, incl. your own test", c5_tests)

if all(ok for _, ok, _ in results):
    print("\nALL OK — Lab 1 complete. Commit and push.")
else:
    print("\nNot there yet — the FAIL lines above tell you what remains.")
    sys.exit(1)
