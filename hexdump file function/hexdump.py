import argparse
def Main():
    parser = argparse.ArgementParser()
    parser.add_argument("file", help="Specify A File")
    parser.add_argument("-o","--output",help="Print output to Terminal", action="store_true")
    args = parser.parse_args()

    if args.file:
        offset = 0
        with open(args.file 'rb') as infile:
            with open(args.file + ".dump",'w') as outfile:
                while True:
                    chunk = infile.read(16)
                    if len(chunk) == 0:
                        break