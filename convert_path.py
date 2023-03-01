# TODO: convert to use Argparse library 

from pathlib import PureWindowsPath, PurePosixPath
import sys, getopt, pprint as pp

def to_unix(path):
    return str(PurePosixPath(path)).strip(" \"\'")

def to_windows(path):
    return str(PureWindowsPath(path)).strip(" \"\'")


if __name__ == "__main__":
    options, args = getopt.getopt(sys.argv[1:], 
                                    "wulp",
                                    ["windows",
                                        "linux",
                                        "unix" ,
                                        "posix" 
                                        ])

    if (len(options)==0):
        print("At least one argument (w, u, l, or p) is required")
        sys.exit()
    
    path = args[0]

    for opt, arg in options:
        if opt in ['-w', '--windows']:
            print(f"Windows Form of path: \n\"{to_windows(path)}\"")
        elif opt in ['-u', '--unix', '-l', '--linux', '-p', '--posix']:
            print(f"Posix Form of path: \n\"{to_unix(path)}\"")
        else:
            print("Unhandled option\n")



