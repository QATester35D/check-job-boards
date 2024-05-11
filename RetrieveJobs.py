from selenium import webdriver
from selenium.webdriver.common.by import By
from CimpressCareers import getJobsFromCimpress
from GoogleCareers import getJobsFromGoogle
from LockheedMartinCareers import getJobsFromLockheed
from AllStateCareers import getJobsFromAllState
from EngageCareers import getJobsFromEngage

getJobsFromCimpress()
getJobsFromGoogle()
getJobsFromLockheed()
getJobsFromAllState()
getJobsFromEngage()
