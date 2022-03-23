
import platform

def main():
    message()

def message():
    print('this is the version for python {}'.format(platform.python_version()))

if __name__ == '__main__':main()
