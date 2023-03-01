"""
This module contains methods which can be used for mobile interruption
"""
from subprocess import call

from appium.webdriver.connectiontype import ConnectionType


class Device:
    @staticmethod
    def get_network_connection(driver):
        return driver.network_connection

    @staticmethod
    def set_connection_type(driver, connection_type):
        if connection_type.upper() in 'WIFI_ONLY':
            driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif connection_type.upper() in 'DATA_ONLY':
            driver.set_network_connection(ConnectionType.DATA_ONLY)
        elif connection_type.upper() in 'AIRPLANE_MODE':
            driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        elif connection_type.upper() in 'ALL_NETWORK_ON':
            driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        elif connection_type.upper() in 'OFFLINE':
            driver.set_network_connection(ConnectionType.NO_CONNECTION)

    @staticmethod
    def click_on_home_button(driver):
        driver.press_keycode(3)

    @staticmethod
    def click_on_back_button(driver):
        driver.press_keycode(4)

    @staticmethod
    def click_on_menu_button(driver):
        driver.press_keycode(82)

    @staticmethod
    def restart_device():
        # only for windows with android
        call(['cmd.exe', '/c', 'adb reboot'])

    @staticmethod
    def shutdown_device():
        # only for windows with android
        call(['cmd.exe', '/c', 'adb shell reboot -p'])
