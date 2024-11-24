#! /usr/bin/env python3

if __name__ == '__main__':
    import src.app

    try:
        src.app.App().round()
    except KeyboardInterrupt:
        pass
else:
    import sys

    sys.stderr.write('Do not import the main file.\n')
    exit()
