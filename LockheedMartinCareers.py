from selenium import webdriver
from selenium.webdriver.common.by import By
from _global import launchBrowserAndURL

#Lockheed Martin - get results count for searching on "test" in Colorado Springs
def getJobsFromLockheed():
    urlLM="https://www.lockheedmartinjobs.com/category/test-engineering-jobs/694/57647/1"
    browserDriver=launchBrowserAndURL(urlLM)
    try:
        resultsText=browserDriver.find_element(By.ID, "search-results-list").text
        jobResultsString=resultsText.split(" ")
        print ("Lockheed Martin - the results count for searching on \"Test Engineering Jobs\" is: ",jobResultsString[4])
        if int(jobResultsString[4]) > 0:
            print("URL for Lockheed Martin test jobs is: ",urlLM)
    except:
        print ("Lockheed Martin has no Test jobs.")
    browserDriver.quit()