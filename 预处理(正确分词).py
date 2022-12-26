with open('测试预料.txt', 'r', encoding='utf-8') as f:
    with open('预处理后(正确分词)', 'w', encoding='utf-8') as f1:
        content = f.readlines()

        for line in content:
            tmp = ''
            cnt = 0
            i = 0
            tmp_mem = ''
            for mem in line:
                i += 1
                if mem != ' ' and (mem > 'z' or mem < 'a') and mem != '\t' and cnt > 1:
                    if tmp_mem == mem and mem == '/' or i == len(line) - 2:
                        continue
                    tmp += mem
                    tmp_mem = mem
                cnt += 1

            f1.write(tmp)


f1.close()
f.close()