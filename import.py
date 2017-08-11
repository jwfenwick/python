import os


def main():
    try :
        os.mkdir("/tmp/foo")
    except:
        print "mkdir failed"


if __name__ == "__main__":
    main()


