from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


seqs2 = []
for i in range(20):
    for s1 in ['A', 'N', 'C']:
        for s2 in ['A', 'N', 'C']:
            for s3 in ['A', 'C']:
                s4 = 'X'
                seq = s1 + s2 + 'X' + s4
                #print(seq)
                seqs2.append(seq)
print(seqs2)
import sys
sys.exit()


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# driver = webdriver.Chrome(r'C:\Users\jchaves6\PycharmProjects\Retention\chromedriver')
driver.maximize_window()
url="http://agadir.crg.es/"
driver.get(url)
login = driver.find_element_by_xpath('//*[@id="rg670"]/tbody/tr/td[6]/a')
login.click()

usernameA = 'Andreach16'
username = driver.find_element_by_xpath('//*[@id="rg4865"]/tbody/tr/td/div/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/input')
username.send_keys(usernameA)
sleep(0.5)

passwordA = 't9AjQoyCHXqq4Jnk'
password = driver.find_element_by_xpath('//*[@id="rg4865"]/tbody/tr/td/div/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input')
password.send_keys(passwordA)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@id="rg4865"]/tbody/tr/td/div/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/input')
sign_in_button.click()
sleep(0.5)


sequences = ['NNRDQIIFMVGRG', 'NTRDEAEFMVGRG']
results = []

for seq in sequences:
    toolB = driver.find_element_by_xpath(
        '/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/div/div[1]/a')
    toolB.click()
    sleep(0.5)

    sequence_input = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table/tbody/tr/td/div/form/table/tbody/tr/td/textarea')
    sequence_input.send_keys(seq)
    sleep(0.5)

    Next_button = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table/tbody/tr/td/div/form/input')
    Next_button.click()
    sleep(0.5)

    checkbox_button = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table/tbody/tr/td/div/form/input[7]')
    checkbox_button.click()
    sleep(0.5)

    Next_button2 = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table/tbody/tr/td/div/form/input[8]')
    Next_button2.click()
    sleep(0.5)

    Next_button3 = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table/tbody/tr/td/div/form/table/tbody/tr[3]/td/input')
    Next_button3.click()
    sleep(0.5)

    Output1 = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/table/tbody/tr/td/div/table/tbody/tr[3]/td/a')
    Output1.click()
    sleep(0.5)

    r2 = driver.page_source
    s2 = BeautifulSoup(r2, 'html.parser')
    results.append([seq, float(s2.text.split('\n')[-2].split('\t')[1])])
    driver.execute_script("window.history.go(-1)")

print(results)
driver.close()
