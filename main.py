from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import datefinder
import datetime
import sys
from pytube import YouTube

"""get name of video and video link"""
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
driver.get("https://www.youtube.com/c/Level1Techs/videos")
level1TechsURLTitle = driver.find_element_by_partial_link_text("Level1 News")
level1TechsURL = level1TechsURLTitle.get_attribute("href")

"""check video date, convert to string and concatenate"""
level1TechsURLTitleString = str(level1TechsURLTitle.text)
split_string = level1TechsURLTitleString.split(":", 1)
substring = split_string[0]
matches = list(datefinder.find_dates(substring))
datePod = None
if len(matches) > 0:
    datePod = matches[0]
datePodString = str(datePod)
datePodStringCon = datePodString.split(" ", 1)
datePodStringConSub = datePodStringCon[0]

"""check if podcasts is already downloaded"""
previousPodsR = open("/home/alex/PycharmProjects/YoutubeToAudioToPhone/previousPods.txt", "r")
lastPod = previousPodsR.readline()
if str(lastPod) == level1TechsURLTitleString:
    driver.quit()
    previousPodsR.close()
    sys.exit()
elif str(lastPod) != level1TechsURLTitleString:
    previousPodsR.close()
    previousPodsW = open("/home/alex/PycharmProjects/YoutubeToAudioToPhone/previousPods.txt", "w")
    previousPodsW.write(level1TechsURLTitleString)
    previousPodsW.close()

"""get current date and convert to string"""
date = datetime.date.today()
dateString = str(date)

"""quit selenium"""
driver.quit()

"""download and name audio file"""
download = None
if dateString == datePodStringConSub:
    download = YouTube(str(level1TechsURL)).streams.get_audio_only().download(
        output_path='/home/alex/Documents/Projects/YoutubeToAudioToPhone/', filename=level1TechsURLTitleString)

"""CLEAN UP,
MAKE CHECK FOR VIDEO EVERY HOUR"""
