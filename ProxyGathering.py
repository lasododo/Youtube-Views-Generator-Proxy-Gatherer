from selenium import webdriver
import time, os

chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver')
browser = webdriver.Chrome(chromedriver)
for z in range(1, 9):
    try:
        if str(z) == "1":
            browser.get('https://free-proxy-list.net/')
            time.sleep(3)

            xpath = '//*[@id="proxylisttable"]/tbody/tr[1]/td[1]'
            xxpath = '//*[@id="proxylisttable"]/thead/tr/th[7]'
            xxxpath = '//*[@id="proxylisttable"]/tbody/tr['

            print('1')
            browser.find_element_by_xpath(xxpath).click()
            time.sleep(2)
            print('2')
            browser.find_element_by_xpath(xxpath).click()
            time.sleep(2)
            print('3')

            def start():
                for x in range(1, 20):
                    u1 = browser.find_element_by_xpath('//*[@id="proxylisttable"]/tbody/tr[' + str(x) + ']/td[1]').text
                    u2 = browser.find_element_by_xpath('//*[@id="proxylisttable"]/tbody/tr[' + str(x) + ']/td[2]').text
                    z = browser.find_element_by_xpath(xxxpath + str(x) + ']/td[7]').text
                    if str(z) == "yes":
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + ':' + str(u2) + '\n')
                            myfile.close()
                        print("IP Written")
                    else:
                        print("Uz niesu")
                        break
                    print(str(u1) + ':' + str(u2))

            def start1():
                number = 4
                print('5')
                for xx in range(20):
                    try:
                        print('6')
                        start()
                        print('7')
                        time.sleep(2)
                        print('button up')
                        link = '//*[@id="proxylisttable_paginate"]/ul/li[{}]/a'.format(number)
                        browser.find_element_by_xpath(
                            link).click()
                        print('button down')
                        time.sleep(2)
                        if number < 7:
                            number += 1
                    except:
                        pass
            start1()

        elif str(z) == "2":
            browser.get('http://www.gatherproxy.com/proxylist/country/?c=Germany')
            time.sleep(3)

            def start():
                for x in range(3, 27):
                    try:
                        u1 = browser.find_element_by_xpath('//*[@id="tblproxy"]/tbody/tr[' + str(x) + ']/td[2]').text
                        u2 = browser.find_element_by_xpath('//*[@id="tblproxy"]/tbody/tr[' + str(x) + ']/td[3]/a').text
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + ':' + str(u2) + '\n')
                            myfile.close()
                        print("IP Written")
                        print(str(u1) + ':' + str(u2))
                    except:
                        print('passin the world')
            start()

        elif str(z) == "3":
            browser.get('https://www.proxynova.com/proxy-server-list/country-ar/')
            time.sleep(3)

            def start():
                for x in range(2, 34):
                    try:
                        u1 = browser.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr['
                                                           + str(x) + ']/td[1]/abbr').text
                        u2 = browser.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr['
                                                           + str(x) + ']/td[2]/a').text
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + ':' + str(u2) + '\n')
                            myfile.close()
                        print("IP Written")
                        print(str(u1) + ':' + str(u2))
                    except:
                        print('passin the world')
            start()

        elif str(z) == "4":
            browser.get('https://www.proxynova.com/proxy-server-list/country-de/')
            time.sleep(3)

            def start():
                for x in range(2, 34):
                    try:
                        u1 = browser.find_element_by_xpath(
                            '//*[@id="tbl_proxy_list"]/tbody[1]/tr[' + str(x) + ']/td[1]/abbr').text
                        u2 = browser.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[' + str(x) +
                                                           ']/td[2]/a').text
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + ':' + str(u2) + '\n')
                            myfile.close()
                        print("IP Written")
                        print(str(u1) + ':' + str(u2))
                    except:
                        print('passin the world')


            start()

        elif str(z) == "5":
            browser.get('https://www.proxynova.com/proxy-server-list/country-ru/')
            time.sleep(3)

            def start():
                for x in range(2, 34):
                    try:
                        u1 = browser.find_element_by_xpath(
                            '//*[@id="tbl_proxy_list"]/tbody[1]/tr[' + str(x) + ']/td[1]/abbr').text
                        u2 = browser.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr['
                                                           + str(x) + ']/td[2]/a').text
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + ':' + str(u2) + '\n')
                            myfile.close()
                        print("IP Written")
                        print(str(u1) + ':' + str(u2))
                    except:
                        print('passin the world')


            start()

        elif str(z) == "6":
            browser.get('https://www.proxynova.com/proxy-server-list/country-us/')
            time.sleep(3)

            def start():
                for x in range(2, 34):
                    try:
                        u1 = browser.find_element_by_xpath(
                            '//*[@id="tbl_proxy_list"]/tbody[1]/tr[' + str(x) + ']/td[1]/abbr').text
                        u2 = browser.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr['
                                                           + str(x) + ']/td[2]/a').text
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + ':' + str(u2) + '\n')
                            myfile.close()
                        print("IP Written")
                        print(str(u1) + ':' + str(u2))
                    except:
                        print('passin the world')
            start()

        elif str(z) == "7":
            browser.get('http://www.freeproxylists.net/')
            time.sleep(3)

            def start():
                for x in range(2, 53):
                    try:
                        u1 = browser.find_element_by_xpath(
                            '/html/body/div[1]/div[2]/table/tbody/tr[' + str(x) + ']/td[1]/a').text
                        u2 = browser.find_element_by_xpath('/html/body/div[1]/div[2]/table/tbody/tr['
                                                           + str(x) + ']/td[2]').text
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + ':' + str(u2) + '\n')
                            myfile.close()
                        print("IP Written")
                        print(str(u1) + ':' + str(u2))
                    except:
                        print('passin the world')

            number = 1
            for xx in range(23):
                if xx == 2:
                    pass
                else:
                    start()
                    tag = '/html/body/div[1]/div[2]/div[3]/a[{}]'.format(number)
                    browser.find_element_by_xpath(tag).click()
                    time.sleep(2)

        elif str(z) == "8":

            browser.get('https://hidemy.name/en/proxy-list/?type=hs&start=64#list')
            time.sleep(3)

            def start():
                for x in range(1, 64):
                    try:
                        u1 = browser.find_element_by_xpath('//*[@id="content-section"]/section[1]/div/table/tbody/tr['
                                                           + str(x) + ']/td[1]').text
                        u2 = browser.find_element_by_xpath('//*[@id="content-section"]/section[1]/div/table/tbody/tr['
                                                           + str(x) + ']/td[2]').text
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + ':' + str(u2) + '\n')
                            myfile.close()
                        print("IP Written")
                        print(str(u1) + ':' + str(u2))
                    except:
                        print('passin the world')

            def start1():
                start()
                browser.find_element_by_xpath('//*[@id="content-section"]/section[1]/div/div[4]/ul/li[3]/a').click()
                time.sleep(1)
                for xx in range(5, 11):
                    if xx == 10:
                        for xxx in range(8):
                            start()
                            link = '//*[@id="content-section"]/section[1]/div/div[4]/ul/li[{}]/a'.format(xx)
                            browser.find_element_by_xpath(link).click()
                            time.sleep(1)
                    else:
                        start()
                        link = '//*[@id="content-section"]/section[1]/div/div[4]/ul/li[{}]/a'.format(xx)
                        browser.find_element_by_xpath(link).click()
                        time.sleep(1)

                for xx in range(3):
                    start()
                    browser.find_element_by_xpath(
                        '//*[@id="content-section"]/section[1]/div/div[4]/ul/li[12]/a').click()
                    time.sleep(1)
                browser.find_element_by_xpath('//*[@id="content-section"]/section[1]/div/div[4]/ul/li[11]/a').click()
                time.sleep(1)
                start()
                browser.find_element_by_xpath('//*[@id="content-section"]/section[1]/div/div[4]/ul/li[10]/a').click()
                time.sleep(1)

            start1()

        elif str(z) == "9":

            browser.get('http://spys.one/en/http-proxy-list/')
            time.sleep(3)

            el = browser.find_element_by_xpath('//*[@id="xpp"]')
            for option in el.find_elements_by_tag_name('option'):
                if option.text == '500':
                    option.click()
                    break

            def start():
                for x in range(3,502):
                    try:
                        u1 = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr['
                                                           + str(x) + ']/td[1]/font[2]').text
                        with open("proxiny.txt", "a") as myfile:
                            myfile.write(str(u1) + '\n')
                            myfile.close()
                        print("IP Written")
                        print(u1)
                    except:
                        print('ip passed')
            start()
    except:
        print('Error Occured')
