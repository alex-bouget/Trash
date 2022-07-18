import kromblast
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--workpath", help="Set the workpath, with kromblast.ini")

if __name__ == "__main__":
    dir_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(dir_path)
    args = parser.parse_args()
    if args.workpath:
        dir_path = os.path.abspath(args.workpath)
    kromblast.Kromblast(
        dir_path,
        os.path.join(dir_path, "kromblast.ini")
    ).show()
