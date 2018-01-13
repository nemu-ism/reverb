import sys
import login

try:
    api = login.api
except:
    print("system has stopped")
    sys.exit()



if __name__ == '__main__':
    try:
        api = login.api
    except:
        print("system has stopped")
        sys.exit()