#Test url: https://engagestaff.jobs.net/jobs?keywords=test&location=
## Generates "No Jobs Found"
#Billing url: https://engagestaff.jobs.net/jobs?keywords=Billing&location=
## Generates "2 Billing Jobs"
#id="job-count"
from selenium import webdriver
from selenium.webdriver.common.by import By
from _global import launchBrowserAndURL

#Engage - get results count for searching on "test" 
def getJobsFromEngage():
  urlLM="https://engagestaff.jobs.net/jobs?keywords=test&location="
  browserDriver=launchBrowserAndURL(urlLM)
  try:
    resultsText=browserDriver.find_element(By.ID, "job-count").text
    jobResultsString=resultsText.split(" ")
    print ("Engage - the results count for searching on \"test, Information Technology\" is: ",jobResultsString[0])
    if int(jobResultsString[0]) > 0:
      print("URL for Engage test jobs is: ",urlLM)
  except:
    resultsText=browserDriver.find_element(By.ID, "jobs-found").text
    if resultsText == "No Jobs Found":
        print ("Engage has no Test jobs.")
    else:
        print ("There was a problem on the page, resultsText was: ",resultsText)
  browserDriver.quit()