from plyer import notification
import time
if __name__ == '__main__':

    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is vital for better mental health, increased concentration",
            app_icon="D:/notification/try.ico",
            timeout=5)
        time.sleep(20)


# pythonw .new.py then run