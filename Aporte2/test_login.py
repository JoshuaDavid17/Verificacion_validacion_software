import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


# ---------- TEST 1: LOGIN VALIDO ----------
def test_login_valido(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    mensaje = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "logged into" in mensaje.lower()


# ---------- TEST 2: LOGIN INVALIDO ----------
def test_login_invalido(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("password_invalida")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "invalid" in error.lower()


# ---------- TEST 3: CASO LIMITE (CAMPOS VACIOS) ----------
def test_login_campos_vacios(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "username")))
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "invalid" in error.lower()
