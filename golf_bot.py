from selenium import webdriver
from secrets import account_number, account_password, days_from_now, main, golfer_one, golfer_two, golfer_three
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import sys
from datetime import timedelta, date
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GolfBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1400,1000)

    def login(self, tee_time):
        self.driver.get('https://bearcreekcc.com')

        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="node-13"]/div/div/p/a/img')
        sign_in_btn.click()

        act_num = self.driver.find_element_by_xpath('//*[@id="edit-name"]')
        act_num.send_keys(account_number)

        act_pswrd = self.driver.find_element_by_xpath('//*[@id="edit-pass"]')
        act_pswrd.send_keys(account_password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="edit-submit"]')
        login_btn.click()

        book_btn = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/ul/li[1]/a')
        book_btn.click()

        self.driver.switch_to_window(self.driver.window_handles[1])
        member_btn = self.driver.find_elements_by_xpath(f"//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZЙ', 'abcdefghijklmnopqrstuvwxyzй'), '{main.lower()}')]")
        member_btn[0].click()

        EndDate = date.today() + timedelta(days=days_from_now)
        EndDate = str(EndDate)
        day = EndDate.split('-')
        lst = list(day[2])
        if lst[0] == '0':
            lst.remove(lst[0])
        day = ''.join(map(str, lst))
        date_btn = self.driver.find_elements_by_xpath(f"//a[@class='ui-state-default' and (text() = '{day}')]")
        date_btn[0].click()


        time_btn = self.driver.find_elements_by_xpath(f"//*[contains(text(), '12:00')]")
        time_btn[len(time_btn)-1].click()


        popup = self.driver.find_elements_by_xpath('/html/body/div[4]')


        if len(popup) >= 1:
            accept_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div[4]/div/button[2]')
            accept_btn.click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="slot_player_row_0"]/td[4]/select/option[2]')))
        self.driver.find_element_by_xpath('//*[@id="slot_player_row_0"]/td[4]/select/option[2]').click()

        if golfer_one != '':
            golfer_one_title = golfer_one.title()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="slot_player_row_1"]/td[3]/input')))
            golfer_one_input = self.driver.find_elements_by_xpath('/html/body/div[2]/div[4]/div[6]/div[1]/div/div[2]/form/table/tbody[1]/tr[2]/td[3]/input')
            golfer_one_input[0].send_keys(golfer_one_title)
            self.driver.find_element_by_xpath('//*[@id="slot_player_row_1"]/td[4]/select/option[2]').click()


        if golfer_two != '':
            golfer_two_title = golfer_two.title()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="slot_player_row_2"]/td[3]/input')))
            golfer_two_input = self.driver.find_elements_by_xpath('//*[@id="slot_player_row_2"]/td[3]/input')
            golfer_two_input[0].send_keys(golfer_two_title)
            self.driver.find_element_by_xpath('//*[@id="slot_player_row_2"]/td[4]/select/option[2]').click()


        if golfer_three != '':
            golfer_three_title = golfer_three.title()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="slot_player_row_3"]/td[3]/input')))
            golfer_three_input = self.driver.find_elements_by_xpath('//*[@id="slot_player_row_3"]/td[3]/input')
            golfer_three_input[0].send_keys(golfer_three_title)
            self.driver.find_element_by_xpath('//*[@id="slot_player_row_3"]/td[4]/select/option[2]').click()


        submit_btn = self.driver.find_elements_by_xpath('//*[@id="main"]/div[6]/div[1]/div/div[3]/a[2]')
        submit_btn[0].click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[4]/div/button/span')))
        finish_btn = self.driver.find_element_by_xpath('/html/body/div[5]/div[4]/div/button/span')
        finish_btn.click()

        


        f=open("times.txt", 'a+')
        f.write(f"{main}, {golfer_one_title}, {golfer_two_title}, {golfer_three}, {EndDate}, {tee_time} \r\n")



if __name__== "__main__":
    bot = GolfBot()
    bot.login(str(sys.argv[1]))