from selenium import webdriver
import time
import threading
import os

amount = 4

links = [
    'https://www.youtube.com/......',
]


def funk(proxy, link_to_vid):
    link = link_to_vid
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % str(proxy))
    chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
    chrome = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    time.sleep(3)
    chrome.get(link)
    time.sleep(2)
    chrome.get(link)
    time.sleep(30)
    try :
        chrome.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string')
        with open("proxiny-fuknce.txt", "a") as myfile:
            myfile.write(str(proxy))
        print("found and printed")
        chrome.close()
    except:
        chrome.close()
        print('Nic sa nenaslo')


for link in links:
    f = open('proxiny.txt')
    line = f.readline()
    x = 1
    xx = 0
    while line:
        if xx < amount:
            print(line)
            line = f.readline()
            try:
                threading.Timer(40, funk, [line, link]).start()
            except Exception as e:
                print(e)
            time.sleep(1)
            x += 1
            xx += 1
            print(x)

        else:
            time.sleep(100)
            for x in range(1, 10):
                try:
                    xzxzx = 'os.system("taskkill /f /im chrome.exe")'
                    os.system("killall 'Google Chrome'")
                except:
                    print("NoMore")
            time.sleep(10)
            xx = 0

    f.close()
