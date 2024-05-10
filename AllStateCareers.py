from selenium import webdriver
from selenium.webdriver.common.by import By
from _global import launchBrowserAndURL

#AllState - get results count for searching on "test" in Colorado Springs
def getJobsFromAllState():
  urlLM="https://www.allstate.jobs/job-search-results/?keyword=test&locationType=Remote&category[]=Information%20Technology"
  browserDriver=launchBrowserAndURL(urlLM)
  try:
    resultsText=browserDriver.find_element(By.ID, "live-results-counter").text 
    print ("AllState - the results count for searching on \"test, Information Technology\" is: ",resultsText)
    if int(resultsText) > 0:
      print("URL for AllState test jobs is: ",urlLM)
  except:
    print ("AllState has no Test jobs.")
  browserDriver.quit()