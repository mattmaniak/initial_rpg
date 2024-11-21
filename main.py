#! /usr/bin/env python3

if __name__ == '__main__':
    from src.app import App
    try:
        App().round()
    except KeyboardInterrupt:
        pass
else:
    from sys import stderr
    stderr.write('Do not import the main file.\n')
    exit()
