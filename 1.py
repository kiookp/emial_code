import requests
import pyperclip

# 从文件中读取邮箱账号和密码
with open('1.txt', 'r') as file:
    account_data = file.readlines()

if len(account_data) >= 1:
    email_data = account_data[0].strip().split('----')
    email_address = email_data[0]
    email_password = email_data[1]


print("邮箱账号:", email_address)
# print("邮箱密码:", email_password)

url = 'my_url'
data = {'email': email_address, 'password': email_password}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('成功！')
    code = response.json()['code']
    print('验证码:', code)
    pyperclip.copy(code)
    print('验证码已复制到剪贴板！')
else:
    print('错误:', response.json()['error'])
