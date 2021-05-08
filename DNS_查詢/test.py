
DN = input('請輸入要查詢網域名稱 ：')
DN_type = str(input('請輸入要查詢 Record 種類 A or NS :'))
print(DN_type)

if 'A' in DN_type:
    pass
elif 'NS' in DN_type:
    pass
else:
    print("請確認輸入查詢 Type")
    break


#score = int(input("score:"))
#if score >= 60:
#    print("成績及格!")
#else:
#    print("不及格，被當了!")