from selenium import webdriver
from selenium.webdriver.common.by import By
from _global import launchBrowserAndURL

#Cimpress - get results count for searching on "test"
def getJobsFromCimpress():
    urlLM="https://jobs.vista.com/Cimpress-Technology/search/?createNewAlert=false&q=test&locationsearch=&optionsFacetsDD_country=&optionsFacetsDD_facility=&optionsFacetsDD_department="
    browserDriver=launchBrowserAndURL(urlLM)
    try:
        resultsText=browserDriver.find_element(By.CSS_SELECTOR, "b:nth-child(2)").text
        print ("Cimpress - the results count for searching on \"test\" is: ",resultsText)
        if int(resultsText) > 0:
            print("URL for Cimpress test jobs is: ",urlLM)
    except:
        print ("Cimpress has no Test jobs.")
    browserDriver.quit()