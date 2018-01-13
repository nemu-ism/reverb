import sys
import twitter
import login

if __name__ == '__main__':
    try:
        login()
    except:
        print("system stopped")
        sys.exit()