# Bot-Auto-Survey-KHS-V2
This repository contains tools for filling out surveys of courses and lecturers as well as facilities and services available at Universitas Mercu Buana. This tool specifically auto-completes surveys with commands that you can set, allowing users to specify their answers and making it easy and fast to use. This tool accommodates the answers to each section of the question according to the available answer options, Expectations, and Satisfaction, ensuring to shorten the time in answering all surveys by running the program once and having flexibility and accuracy in answering each question.

## Requirements
There are several conditions that must be met to be able to run this program including:

#### **1. [Visual Stiudio Code](https://code.visualstudio.com/download)**
There are many code editor options that you can run but I strongly recommend using the [Visual Stiudio Code](https://code.visualstudio.com/download), because the ecosystem is very good and supports programmers to write, create, manage, improve, and run a program or system from any part of a particular part in a technology used. Another reason is because [Visual Stiudio Code](https://code.visualstudio.com/download) has a very complex appearance and usability, and supports many existing tach stacks, as well as being able to provide many extensions that support and facilitate programmers.

#### **2. [Python](https://www.python.org/downloads/)**
Make sure you have installed [Python](https://www.python.org/downloads/) before, or if not you can install Python first on the official website (or you can click on the sub title above). If you have downloaded python.exe run it to perform the installation process which you can follow through the information provided. The important thing to note in installing [Python](https://www.python.org/downloads/) is to pay attention to the version because to be able to run a certain program you must use a certain version of [Python](https://www.python.org/downloads/) to be able to run the program, in this case I suggest the most recent version or at least Python 3.12 and adjust it for the operating system version you are using.

## Installation
#### **1. [Bot-Auto-Survey-KHS-V2](https://github.com/arifsuz/Bot-Auto-Survey-KHS-V2)**
You can download this repository in zip form and you can extract it first to open and run the program, but I strongly recommend that you just clone it to make your work easier and faster.
- Copy this command `git clone https://github.com/arifsuz/Bot-Auto-Survey-KHS-V2.git`.
- Paste it into the command prompt or terminal and make sure the directory where you save the project is the way you want it.
- After you paste it, press the enter button to run the cloning process.
- Then open the directory with the command `cd Bot-Auto-Survey-KHS`.

#### **2. [Selenium WebDriver](https://pypi.org/project/selenium/)**
If you are starting with desktop website or mobile website test automation, then you will be using the WebDriver API. WebDriver uses the browser automation API provided by the browser vendor to control the browser and run tests. It's as if the user is actually operating the browser. Since WebDriver does not require its API to be compiled with the application code, it is not intrusive. Therefore, you test the same application that you launch directly. WebDriver drives the browser natively, as the user does, either locally or on a remote machine using a Selenium server, marking a leap forward in terms of browser automation. Selenium WebDriver refers to the language binding and code implementation of individual browser controllers. It is usually referred to simply as WebDriver. Important notes for installing : 
- Make sure you open the terminal in the directory you want or in a place that is in the same directory as this program.
- then run the `pip install Selenium` in the command line or 
- Make sure the Selenium library is installed correctly and successfully, if there are errors or problems you can visit the documentation website or can click the sub title above.

## Usage

#### **1. Customize the code below with your SIA or SSO account.**
```
# ========= SSO MERCUBUANA ACCOUNT ========= #
username = "41523010XXX" # REPLACE WITH STUDENT IDENTIFICATION NUMBER (NIM)
password = "123456789"  # REPLACE WITH YOUR SIA PASSWORD
# ========================================== #
```

#### **2. You can customize the waiting time of each process, and set its auto-answer.**
```
# ======================= SUPPORT ============================ #
# Waiting Time of Each Process
delay = 0.3 #CUSTOMIZE THE DELAY TIME OF EACH PROCESS YOU WANT.

# Answer Options
# HARAPAN :                 # KEPUASAN :
# - Tidak Penting           # - Tidak Puas
# - Cukup Penting           # - Kurang Puas
# - Penting                 # - Puas
# - Sangat Penting          # - Sangat Puas

# Survey Answers
harapan = 'Penting'
kepuasan = 'Puas'
# ============================================================ #
```
Make sure you adjust the time in seconds accordingly, and also choose the answer that suits you.

#### **3. Adjust the number of courses being taken in this semester.**
```
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
```
### This program will fill out a survey on each course, make sure the program is in accordance with the number of courses you are taking this semester. If you only take 7 courses, then delete the program with tags `COURSE 8` and `COURSE 9`. As in the example below.
```
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
```

#### **4. How to run the program**
After the program has been adjusted to your needs, the next step is to run a program called `main.py`, namely by opening a terminal in Visual Studio Code by pressing the `Terminal>New Terminal` menu or you can use a shortcut on the keyboard by pressing the `CTRL key +SHIFT+`` simultaneously.

Then type `python main.py` in the terminal then press ENTER to run the program.

## Video Customize Guide
Watch the video below for a full tutorial on how to run the program.


## Contributions

If you want to contribute to this project, you can follow these steps:

1. Fork this repository to your GitHub account.
2. Clone the forked repository to your local computer.
3. Move to the project directory with `cd <repo-name>`.
4. Create a new branch for the feature or fix you want to add with `git checkout -b <branch-name>`.
5. Make necessary changes to the code.
6. Commit your changes with a clear and descriptive message using `git commit -m "Description of changes"`.
7. Push the branch to your GitHub repository with `git push origin <branch-name>`.
8. Open the forked repository page on GitHub and create a new pull request.
9. Fill out the pull request description to clearly explain the changes you made.
10. Wait for feedback and discussion from the repository owner.

Make sure to follow the contribution rules and guidelines set by this project. This may include things like code of conduct, writing style, and code review process.

The pull request process involves proposing code changes to the main repository. Once a pull request is created, the repository owner will review your changes and decide whether or not to merge them into the main repository. Discussion and refinement may be required before the pull request can be accepted.

Be sure to understand and follow the pull request process established by this project. This may include steps such as code testing, peer code review, and documentation requirements.

Always communicate with the repository owner and project team to ensure that your contributions meet their needs and expectations.

## Authors
**Developed by :**
**Muhamad Nur Arif**
**(41523010147)**

### 🔗 Link
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://arifsuz.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/arifsuz)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marif8/)
[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/arif_suz/)
