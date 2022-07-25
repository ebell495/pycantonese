#!/usr/local/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import pycantonese

pycantonese.segment("我們")


@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    in_str = fdp.ConsumeString(len(data))

    pycantonese.segment(in_str)


# atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()