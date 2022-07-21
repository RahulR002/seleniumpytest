from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    inputEmail = driver.find_element(By.ID, "email")
    inputEmail.send_keys("rautrahul2012@gmail.com")
    inputPass = driver.find_element(By.ID, "pass")
    inputPass.send_keys("Password@123")
    btnLogin = driver.find_element(By.NAME, "login")
    btnLogin.click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')