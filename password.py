# 密碼重設程式
# 先在程式碼中設定好密碼 password = 'a123456'
# 讓使用者【最多輸入3次密碼】
# 不對的話，就印出"密碼錯誤! 還有_次機會" 
# 對的話，就印出"登入成功!"

password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
    i = i -1
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功!')
        break # 逃出迴圈
    else:
        print('密碼錯誤!')
        if i > 0:
            print('還有', i, '次機會')
        else:
            print('抱歉沒機會嘗試，封鎖帳號XD')
            
        



