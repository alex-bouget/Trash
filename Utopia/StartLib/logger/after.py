import tkinter
import sys


def setup_after_excepthook():

    def _report_exception_with_hook(self):
        sys.excepthook(*sys.exc_info())

    tkinter.Misc._report_exception = _report_exception_with_hook
