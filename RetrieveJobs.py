from selenium import webdriver
from selenium.webdriver.common.by import By
from CimpressCareers import getJobsFromCimpress
from GoogleCareers import getJobsFromGoogle
from LockheedMartinCareers import getJobsFromLockheed

getJobsFromCimpress()
getJobsFromGoogle()
getJobsFromLockheed()
