from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

time.sleep(3)

create=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[1]/div/div[6]/div/a/div/div[1]/div/span/span")
time.sleep(3)

email=driver.find_element(By.ID,"_r_22_")
email.send_keys("yihep76698@icubik.com")

password=driver.find_element(By.ID,"_r_3n_")
email.send_keys("graminsta@123")

month=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[5]/label/div/div/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div/svg")
month1=driver.find_element(By.XPATH,"")

# password=driver.find_element(By.ID,"_R_33d9lplcldcpbn6b5ipamH1_")
# password.send_keys("1234567")
# password.send_keys(Keys.RETURN)
# time.sleep(300)


#id="_R_32d9lplcldcpbn6b5ipamH1_"

#id="_R_33d9lplcldcpbn6b5ipamH1_"

#_r_22_ ph no and email

#_r_3n_  password

#birthday
#month /html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[5]/label/div/div/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div/svg
# day /html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[5]/label/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/svg
# year /html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[5]/label/div/div/div[2]/div/div/div/div/div[3]/div/div/div[1]/div/div/svg

#name 
# _r_4c_

# username _r_4i_