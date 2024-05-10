from selenium import webdriver
# from selenium.webdriver.common.by import By

def launchBrowserAndURL(url):
    browserDriver=webdriver.Firefox()
    browserDriver.get(url)
    browserDriver.set_window_size(1500, 800)
    return(browserDriver)