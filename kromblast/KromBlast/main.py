import kromblast
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("config", help="Set the ini file", type=str)
parser.add_argument("-d", "--dir", "-D", help="Set the workpath. if not used, the workpath is the ini folder", type=str)
args = parser.parse_args()

if __name__ == "__main__":
    ini = os.path.abspath(args.config)
    directory = os.path.dirname(ini)
    kromblast.Kromblast(
        directory,
        ini
    ).show()
