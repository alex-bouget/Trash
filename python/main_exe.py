from LineUp import LineUp

import getopt
import sys
import os


def usage():
    print("Usage: \n" +
          "-m: lum file, Modules loaded (.lum)\n" +
          "-d: modules dir\n" +
          "[-f]: lup file, LineUp code\n" +
          "if -f not use, open the interpreter"
          )


if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "f:m:d:")

    data = {
        "e_type": "print"
    }
    lup = None

    if len(opts) <= 0:
        usage()
        exit(0)

    for opt, arg in opts:
        if opt in ['-f']:
            lup = os.path.abspath(arg)
        elif opt in ['-m']:
            data["lum"] = os.path.abspath(arg)
        elif opt in ['-d']:
            data["m_dir"] = os.path.abspath(arg)
        else:
            usage()
            exit(0)
    if lup is None:
        print("LineUp Interpreter 0.12.31")
        LineUp(**data).console()
    else:
        LineUp(**data).global_variable["l"].execute(lup)
