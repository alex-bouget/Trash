from LineUp import LineUp

import getopt
import sys
import os

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "f:m:d:")

    data = {
        "e_type": "print"
    }
    lup = None

    for opt, arg in opts:
        if opt in ['-f']:
            lup=os.path.abspath(arg)
        elif opt in ['-m']:
            data["lum"] = os.path.abspath(arg)
        elif opt in ['-d']:
            data["m_dir"] = os.path.abspath(arg)
    LineUp(**data).execute(lup)
