#=============================================================================================================================#
    # Author = Muhamad Nur Arif
    # Description = This script is used to fill out the survey form on the Mercubuana PRISMA website.
    # SKS = 24 (9 Courses)
    # Notes : If your number of credits in this semester is less than 24 credits,
    #         then delete the program command with the 'COURSE' tag below. Or you can match the total courses this semester.
#=============================================================================================================================#

# ---------------------------------------------------- Import Module ---------------------------------------------------- #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# ---------------------------------------------------- DATA LIST ---------------------------------------------------- #

# ========= SSO MERCUBUANA ACCOUNT ========= #
username = "41523010XXX" # REPLACE WITH STUDENT IDENTIFICATION NUMBER (NIM)
password = "123456789"  # REPLACE WITH YOUR SIA PASSWORD
# ========================================== #

# ================================ URL & TARGET ================================  #
survey = "https://prima.mercubuana.ac.id/survey/mahasiswa"
target_username = "username"
target_password = "password"
login = '//*[@id="auth"]/div/div/div[2]/div/form/button'
# ================================================================================= #

# ======================= SUPPORT ============================ #

# Waiting Time of Each Process
delay = 0.3 #CUSTOMIZE THE DELAY TIME OF EACH PROCESS YOU WANT.

# Survey Answers
harapan = 'Penting'
kepuasan = 'Puas'
# ============================================================ #

# ---------------------------------------------------- MAIN PROGRAM ---------------------------------------------------- #

# Inisialisasi driver Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Accessing the URL
driver.get(survey)
time.sleep(delay)

# Enter Username Survey PRISMA Mercubuana
username_survey = driver.find_element(By.NAME, target_username)
username_survey.send_keys(username)
time.sleep(delay)

# Enter Pssword Survey PRIMSA Mercubuana
password_survey = driver.find_element(By.NAME, target_password)
password_survey.send_keys(password)
time.sleep(delay)

# Sing In button
login_button = driver.find_element(By.XPATH, login)
login_button.click()
time.sleep(delay)

# ================================ PERIODE SURVEY ================================  #

# Click Button Survey
survey_periode_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[4]/a')
survey_periode_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 3
dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step3"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 4
dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step4"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 5
dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step5"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 6
dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step6"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 7
dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step7"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 8
dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step8"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 9
dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step9"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 10
dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step10"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_submit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)
# ================================================================================= #

# ================================ COURSE 1 ================================  #

#Click Button Course
course1_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[1]/td[9]/a')
course1_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)

# ================================ COURSE 2 ================================  #

# Click Button Course
course2_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[2]/td[9]/a')
course2_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)

# ================================ COURSE 3 ================================  #

# Click Button Course
course2_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[3]/td[9]/a')
course2_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)

# ================================ COURSE 4 ================================  #

# Click Button Course
course2_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[4]/td[9]/a')
course2_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)

# ================================ COURSE 5 ================================  #

# Click Button Course
course2_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[5]/td[9]/a')
course2_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)

# ================================ COURSE 6 ================================  #

# Click Button Course
course2_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[6]/td[9]/a')
course2_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)

# ================================ COURSE 7 ================================  #

# Click Button Course
course2_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[7]/td[9]/a')
course2_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)

# ================================ COURSE 8 ================================  #

# Click Button Course
course2_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[8]/td[9]/a')
course2_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)

# ================================ COURSE 9 ================================  #

# Click Button Course
course2_button = driver.find_element(By.XPATH, '//*[@id="table-pembelajaran-body"]/tr[9]/td[9]/a')
course2_button.click()
time.sleep(delay)

# Step 1
dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step1"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_next = driver.find_element(By.XPATH, '//*[@id="survey-form"]/div[2]/button[2]')
button_next.click()
time.sleep(delay)

# Step 2
dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[1]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[2]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[3]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[4]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[1]/select')
dropdown.click()
dropdown.send_keys(harapan)
time.sleep(delay)

dropdown = driver.find_element(By.XPATH, '//*[@id="step2"]/div[5]/div/div[2]/select')
dropdown.click()
dropdown.send_keys(kepuasan)
time.sleep(delay)

button_sumbit = driver.find_element(By.XPATH, '//*[@id="save-quisioner-mahasiswa"]')
button_sumbit.click()
time.sleep(delay)

button_confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')
button_confirm.click()
time.sleep(delay)
# ================================================================================= #

time.sleep(600)