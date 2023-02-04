import webui
import app as user_src

user_src.init()
user_src.apply_weights()

if __name__ == '__main__':
    webui.api_only()