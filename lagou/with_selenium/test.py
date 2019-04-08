
from selenium import webdriver   #webdriver就是加载你的浏览器驱动，比如我使用的是谷歌，就是Chrome,记住一个小知识，当Chrome不好使的时候，你可以换个内核，往往问题是出现在这
from selenium.webdriver.common.by import By #这几个东西都是固定的，是智能等待所需要用到的1
from selenium.webdriver.support.ui import WebDriverWait #这几个东西都是固定的，是智能等待所需要用到的2
from selenium.webdriver.support import expected_conditions as EC #这几个东西都是固定的，是智能等待所需要用到的3
from lxml import etree   #叉path模块

def start_driver_request():
        lagou = driver.page_source  # 收集当前页信息
        parse(lagou)   #解析方法，传入信息
        try:
            WebDriverWait(driver, 3, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[class="pager_next"]')))    #每当浏览器需要进行交互动作的时候，都必须进行智能等待，不信你取消掉这句试试
        finally:
            driver.find_element_by_css_selector('span[action="next"]').click()
            # windows = driver.current_window_handle  #
            # all_handles = driver.window_handles  #
            # for handle in all_handles:
            #     if handle != windows:
            #         driver.switch_to.window(handle)
            return start_driver_request()

def parse(response):
    soup1 = etree.HTML(response)
    item_job = soup1.xpath('//li/@data-positionname')
    item_company = soup1.xpath('//li/@data-company')
    item_salary = soup1.xpath('//li/@data-salary')
    return print(item_job,item_company,item_salary)

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/list_?city=深圳&cl=false&fromSearch=true&labelWords=&suginput='
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    try:
        WebDriverWait(driver, 3, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[id="submit"]')))
    finally:
        driver.find_element_by_css_selector('input[id="keyword"]').send_keys("python")
        driver.find_element_by_css_selector('input[id="submit"]').click()
        start_driver_request()