import sys
import login
import reverb_controller

if __name__ == '__main__':
    try:
        print("reverbを開始します")
        api = login.Login().login()
        reverb_controller.Main().main(api)
    except:
        print("reverbを終了します")
        sys.exit()