from selenium import webdriver

#driver = webdriver.Firefox(options=opt, executable_path='/hpath/of/geckodriver')
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input("Enter the name of group or user :")
msg = input('Enter the message :')
count=int(input('Enter the count :'))

input('Enter anything after scanning QR code :')

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('p3_M1')	#<div tabindex="-1" class="p3_M1">

for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_class_name('_4sWnG')	#<button class="_4sWnG">
	button.click()

print("Finished....!")