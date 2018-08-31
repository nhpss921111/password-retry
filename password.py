# 密碼重設程式
# 先在程式碼中設定好密碼 password = 'a123456'
# 讓使用者【最多輸入3次密碼】
# 不對的話，就印出"密碼錯誤! 還有_次機會" 
# 對的話，就印出"登入成功!"

password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功!')
        break # 逃出迴圈
    else:
        i = i -1
        print('密碼錯誤! 還有', i, '次機會')
        if i == 0:
            print('封鎖帳號')
            break
        



