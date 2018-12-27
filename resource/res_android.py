import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def get_desired_capabilities(app):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0.0'
    desired_caps['deviceName'] = '1ecdd251'
    desired_caps['app'] = PATH('../application/' + app)
    desired_caps['appPackage'] = 'com.mbayar'
    desired_caps['appActivity'] = 'com.mbayar.intro.SplashScreen'
    desired_caps['autoGrantPermissions'] = 'true'

    return desired_caps

#emulator-5554 = 5.1.1
#52005a21b207b40f = 8.0.0
#S4DQSKM7A6NJNVTC = 4.4.2
#1ecdd251 = 8.0.0