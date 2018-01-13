import sys
import login
import reverb_controller

if __name__ == '__main__':
    reverb = reverb_controller.Main()
    try:
        print("reverbを開始します")
        api = login.Login().login()
        reverb.main(api)
    except:
        print("reverbを終了します")
        sys.exit()