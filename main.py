from configparser import ConfigParser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import datefinder
from datetime import timedelta, date
import sys
from pytube import YouTube
from os import listdir, remove
from os.path import isfile, join

"""get paths"""
config = ConfigParser()
config.read("ENTER THE ABSOLUTE PATH TO YOUR my_paths.ini HERE")
chromeDriverPath = config.get("PATHS", "chromedriver")
previousPodPath = config.get("PATHS", "previousPod")
podcastOut = config.get("PATHS", "podcastOut")

"""get name of video and video link"""
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chromeDriverPath, options=chrome_options)
driver.get("https://www.youtube.com/c/Level1Techs/videos")
level1TechsURLTitle = driver.find_element_by_partial_link_text("Level1 News")
level1TechsURL = level1TechsURLTitle.get_attribute("href")

"""check video date, convert to string and split"""
level1TechsURLTitleString = str(level1TechsURLTitle.text)
split_string = level1TechsURLTitleString.split(":", 1)
substring = split_string[0]
matches = list(datefinder.find_dates(substring))
datePod = None
if len(matches) > 0:
    datePod = matches[0]
datePodString = str(datePod)
datePodStringSplt = datePodString.split(" ", 1)
datePodStringSpltSub = datePodStringSplt[0]

"""check if podcasts is already downloaded"""
previousPodsR = open(previousPodPath, "r")
lastPod = previousPodsR.readline()
if str(lastPod) == level1TechsURLTitleString:
    driver.quit()
    previousPodsR.close()
    sys.exit()
elif str(lastPod) != level1TechsURLTitleString:
    previousPodsR.close()
    previousPodsW = open(previousPodPath, "w")
    previousPodsW.write(level1TechsURLTitleString)
    previousPodsW.close()

    """get current date and convert to string"""
    date = date.today()
    dateString = str(date)

    """quit selenium"""
    driver.quit()

    """download and name audio file"""
    download = None
    if dateString == datePodStringSpltSub:
        download = YouTube(str(level1TechsURL)).streams.get_audio_only().download(
            output_path=podcastOut, filename=level1TechsURLTitleString)

    """delete videos past certain date"""
    daysBeforeDeletion = 3
    onlyFiles = [f for f in listdir(podcastOut) if isfile(join(
        podcastOut, f))]
    deletion_date = date.today() - timedelta(daysBeforeDeletion)
    iterator = 0
    for file in onlyFiles:
        fileDate = list(datefinder.find_dates(onlyFiles[iterator]))
        if not fileDate:
            break
        else:
            if fileDate[0].date() < deletion_date:
                remove(podcastOut + onlyFiles[iterator])
            iterator += 1
