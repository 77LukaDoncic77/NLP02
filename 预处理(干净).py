with open('测试预料.txt','r', encoding='utf-8') as f:
    with open('预处理后(干净).txt', 'w', encoding='utf-8') as f1:
        content = f.readlines()

        for line in content:
            tmp = ''
            tmp1 = ''
            cnt = 0
            for mem in line:
                if cnt > 1 and mem != ' ' and (mem > 'z' or mem < 'a') and mem != '/' and mem != '\t':
                    tmp += mem
                cnt += 1

            f1.write(tmp)


f1.close()
f.close()