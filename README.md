This is a simple python script to download the Level1 News (https://www.youtube.com/channel/UC4w1YQAJMWOz4qtxinq55LQ) video as a podcast. The instructions will also show you how to share the podcast with your phone and how to automate the entire process so you don't even hav to press a button... on linux ;)

Installation:

1. Open youtube_to_phone in your editor of choice
2. Open main.py
3. Enter the absolute path to my_paths.ini into the function config.read(" ") between the quotes
4. Install chromedriver for Selenium
5. Open my_paths.ini
6. Enter path to your chromedriver in chromedriver value
7. Enter path to previousPods.txt (within this directory) into value for previousPod
8. Create folder where you want to store the podcast
9. Go back to my_paths.ini
10. Enter path to where you are storing the podcast into podcastOut value
11. Save main.py and my_paths.ini
12. Run (If Level1 News has been uploaded that day it will be downloaded as a audio file; You will also see that the name of the podcast is saved to previousPods.txt. This is so that if you run this script in the background it will not keep downloading the same file)

Settings:

Set the daysBeforeDeletion variable to the amount of days you would like the podcasts to stay in the drive you are saving them to (default is 3)

How to share the podcast to your phone on linux (Manjaro):

1. Download Samba if it is not already downloaded (sudo pacman -Syu samba)
2. create samba conf file (pamac install samba kdenetwork-filesharing manjaro-settings-samba) (other linux distros: https://wiki.manjaro.org/index.php/Using_Samba_in_your_File_Manager)
3. reboot PC
4. go to samba.conf (/etc/samba/samba.conf)
5. add this to bottom of file:

[sambashare]  
   comment = Samba on Manjaro  
   path = EDIT THIS TO BE THE PATH YOU ARE STORING PODCASTS IN  
   read only = no  
   browseable = yes
   
6. If you did not read what you just copied into your samba.conf, READ THE VALUE FOR path
7. save samba.conf and close the file
8. Open Console
9. type: sudo smbpasswd -a "THE USERNAME YOU USE TO SIGN INTO THE CURRENT USER ON YOUR COMPUTER"
10. Make a password
11. Download a file manager on your phone that allows for SMB (I use https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en_US&gl=US)
12. Open the app and navigate to file sharing
13. Click on your computers name
14. Enter username (your username for your computer) and password (the password you made in the console for samba)
15. You should now have access to your podcast directory on your LAN
16. If listening outside of your home network, copy the file from your podcast directory to a local directory on your phone

How to make this script run in the background on linux:

1. Open Console
2. Run crontab -e
3. Go here: https://crontab-generator.org/
4. Enter your preffered settings and click Generate Crontab Line
5. Copy the crontab line
6. Paste the crontab line into nano, the text editor opened in your console after running crontab -e, press Ctrl o, press Ctrl x)
7. Make sure your computer is on at atleast one of the times you told the cron job to run

CONGRATULATIONS, YOU NOW HAVE LEVEL1 NEWS BEING DOWNLOADED DIRECTLY TO YOUR PHONE AUTOMATICALLY