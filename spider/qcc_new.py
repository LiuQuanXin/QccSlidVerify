# !/usr/bin/python
# coding: utf-8
# time: 2019/6/20

import sys
import time
import json

reload(sys)
sys.setdefaultencoding('utf-8')
import random
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from commen.user_agent_list import new_header

from pyvirtualdisplay import Display
import logging as logger


class BrandSpider(object):

    def __init__(self, task=None):
        self.start = time.time()
        self.flag1 = False
        self.display = None
        # os.system('export DISPLAY=:7')
        # self.display = Display(visible=0, size=(1920, 1080))
        # self.display.start()
        self.task = task
        self.driver = None
        self.maxpage = 10
        self.code = 0
        self.page = []
        option = webdriver.FirefoxOptions()
        path = '/Users/admin/Downloads/geckodriver'
        # option.add_argument('-headless')
        ua = new_header()
        print ua
        # dcap['firefox.page.settings.userAgent'] = ua
        option.set_preference('general.useragent.override', ua)
        option.add_argument('--disable-gpu')
        option.add_argument('--no-sandbox')
        option.add_argument('log-level=5')

        self.kw = {
            'executable_path': path,
            'options': option,
            # 'service_log_path': None
            # 'service_args': ['--ignore-ssl-errors=true']
        }
        self.driver = webdriver.Firefox(**self.kw)
        self.wait = WebDriverWait(self.driver, 20, 0.5)

    def __del__(self):
        self.driver.quit()
        if self.display:
            self.display.stop()
        self.flag1 = True
        logger.info('driver 关闭')

    def move_button(self, pic_button, track):
        ActionChains(self.driver).click_and_hold(pic_button).perform()
        for x in track:
            if isinstance(x, (float, int)):
                ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=random.random() * 2).perform()
            else:
                ActionChains(self.driver).move_by_offset(xoffset=x[0], yoffset=x[1]).perform()
        time.sleep(0.5)
        ActionChains(self.driver).release().perform()

    def crawl(self):
        self.driver.get("http://127.0.0.1:8880/qcc")
        # BTN = self.wait.until(EC.element_to_be_clickable((By.ID, 'nc_1_n1z')))
        # print BTN
        
        while 1:
            try:
                for i in range(1, 7):
                    time.sleep(2)
                    # print self.driver.page_source
                    logger.warning('nc_%s_n1z' % i)
                    btn = self.driver.find_element_by_id('nc_%s_n1z' % i)
                    track = tracks()
                    self.move_button(btn, track)
            except:
                self.driver.get("http://127.0.0.1:8880/qcc")


def tracks(l=310):
    n = 4
    t = [0.0, 1.0, 3.0]
    while n < l:
        tt = random.randint(20, 30)
        n += tt
        t.append(tt)
    logger.warning(t)
    return t


if __name__ == '__main__':
    spider = BrandSpider()
    spider.crawl()
