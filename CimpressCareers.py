from selenium import webdriver
from selenium.webdriver.common.by import By

#Cimpress - get results count for searching on "test"
def getJobsFromCimpress():
    browserDriver=webdriver.Firefox()
    urlCimpress="https://jobs.vista.com/Cimpress-Technology/search/?createNewAlert=false&q=test&locationsearch=&optionsFacetsDD_country=&optionsFacetsDD_facility=&optionsFacetsDD_department="
    browserDriver.get(urlCimpress)
    browserDriver.set_window_size(1500, 800)
    resultsText=browserDriver.find_element(By.CSS_SELECTOR, "b:nth-child(2)").text
    print ("Cimpress - the results count for searching on \"test\" is: ",resultsText)
    if int(resultsText) > 0:
        print("URL for Cimpress test jobs is: ",urlCimpress)
    browserDriver.quit()