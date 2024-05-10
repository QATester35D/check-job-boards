from selenium import webdriver
from selenium.webdriver.common.by import By
from _global import launchBrowserAndURL

#Google - get results count for searching on "test"
def getJobsFromGoogle():
    # browserDriver=webdriver.Firefox()
    # urlGoogle="https://www.google.com/about/careers/applications/jobs/results?has_remote=true&q=test&employment_type=FULL_TIME&target_level=MID&target_level=ADVANCED&location=United%20States#!t=jo&jid=127025001&"
    # browserDriver.get(urlGoogle)
    # browserDriver.set_window_size(1500, 800)
    # resultsText=browserDriver.find_element(By.CSS_SELECTOR, ".mSE5Se .SWhIm").text
    # print ("Google - the results count for searching on \"test, USA, Remote, Mid, Advanced\" is: ",resultsText)
    # if int(resultsText) > 0:
    #     print("URL for Google test jobs is: ",urlGoogle)
    # browserDriver.quit()
    urlLM="https://www.google.com/about/careers/applications/jobs/results?has_remote=true&q=test&employment_type=FULL_TIME&target_level=MID&target_level=ADVANCED&location=United%20States#!t=jo&jid=127025001&"
    browserDriver=launchBrowserAndURL(urlLM)
    try:
        resultsText=browserDriver.find_element(By.CSS_SELECTOR, ".mSE5Se .SWhIm").text
        print ("Google - the results count for searching on \"test, USA, Remote, Mid, Advanced\" is: ",resultsText)
        if int(resultsText) > 0:
            print("URL for Google test jobs is: ",urlLM)
    except:
        print ("Google has no Test jobs.")
    browserDriver.quit()