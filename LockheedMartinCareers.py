from selenium import webdriver
from selenium.webdriver.common.by import By

#Lockheed Martin - get results count for searching on "test" in Colorado Springs
def getJobsFromLockheed():
  browserDriver=webdriver.Firefox()
  urlLM="https://www.lockheedmartinjobs.com/search-jobs/Test/Colorado%20Springs%2C%20CO/694/1/4/6252001-5417618-5420926-5417598/38x83388/-104x82136/50/2"
  browserDriver.get(urlLM)
  browserDriver.set_window_size(1500, 800)
  try:
    resultsText=browserDriver.find_element(By.CSS_SELECTOR, "#search-results-list > p").text   #returns "Showing 15 out of 18 results" so I need to parse this
    jobResultsString=resultsText.split(" ")
    print ("Lockheed Martin - the results count for searching on \"test, USA, Remote, Mid, Advanced\" is: ",jobResultsString[4])
    if int(jobResultsString[4]) > 0:
      print("URL for Lockheed Martin test jobs is: ",urlLM)
  except:
    print ("Lockheed Martin has no Test jobs.")
  browserDriver.quit()
