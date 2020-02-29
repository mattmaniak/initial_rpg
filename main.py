if __name__ == '__main__':
    from src.app import App
    App().run()
else:
    from sys import stderr
    stderr.write('Do not import the main file.\n')
    exit()
