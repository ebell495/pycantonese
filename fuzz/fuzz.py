#!/usr/local/bin/python3
import atheris
import sys

# from logmine_pkg.run import run
with atheris.instrument_imports():
    import pycantonese


@atheris.instrument_func
def TestOneInput(data):
    if len(data) < 1:
        return
    fdp = atheris.FuzzedDataProvider(data)
    option = fdp.ConsumeBytes(1)[0]
    in_str = fdp.ConsumeString(len(data))

    if option % 4 == 0:
        pycantonese.parse_text(in_str)
    elif option % 4 == 1:
        pycantonese.segment(in_str)
    elif option % 4 == 3:
        pycantonese.characters_to_jyutping(in_str)


# atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
# Hacky, but the cli does not like the arguments Mayhem gives it
sys.argv = [sys.argv[0]]
atheris.Fuzz()