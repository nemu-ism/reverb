import sys
import login
import reverb_controller

if __name__ == '__main__':
    try:
        print("ready")
        api = login.Login().login()
        reverb_controller.Main().main(api)
    except:
        print("system has stopped")
        sys.exit()