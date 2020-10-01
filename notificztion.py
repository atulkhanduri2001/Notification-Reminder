from plyer import notification
import time
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "**Please drink water!!",
            message= "Water is an inorganic, transparent, tasteless, odorless, and nearly colorless chemical substance, which is the main constituent of Earth's hydrosphere and the fluids of all known living organisms.",
            # app_icon ="C:\Users\noida\PycharmProjects\pythonProject\Upload to github\notification reminder\Iconsmind-Outline-Glass-Water.ico",
            timeout = 15
        )
        time.sleep(60*60)