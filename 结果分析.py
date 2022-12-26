import csv

# 将词保存成集合形式
def getWord(str):
    list = []
    s = 0
    for word in str.split("/"):
        e = s + len(word)
        list.append((s, e - 1))
        s = e
    return set(list)

# ori是原来的分词，pred是系统预测的输出
def evaluate(pred,ori):
    predSize = len(getWord(pred))
    oriSize = len(getWord(ori))
    rightSize = len(getWord(ori) & getWord(pred))
    # Recall
    R = rightSize / oriSize
    # Precision
    P = rightSize / predSize
    # F-measure
    if P == 0 or R == 0:
        return R, P, 'invalid'
    F = 2 * P * R / (P + R)
    return R, P, F

if __name__ == '__main__':
    # pred_1 = "我/来到/北京/清华/大学/。"
    # pred_2 = "我/来到/北京/清华大学/。"
    # ori = "我/来到/北京/清华大学/。"
    # with open('RPF统计/Results-of-HanLP(粗糙版).csv', 'w', newline="") as f0:
    # with open('RPF统计/Results-of-HanLP(精细版).csv', 'w', newline="") as f0:
    with open('RPF统计/thulac.csv', 'w', newline="") as f0:
        csv_write = csv.writer(f0)
        csv_write.writerow(["Recall", "Precision", "F-measure"])
        with open('actual/预处理后(正确分词).txt', 'r', encoding='utf-8') as f:
            # with open('result/Results-of-HanLP(粗糙版).txt', 'r', encoding='utf-8') as f1:
            # with open('result/Results-of-HanLP(精细版).txt', 'r', encoding='utf-8') as f1:
            with open('result/thulac.txt', 'r', encoding = 'utf-8') as f1:
                a = f.readlines()
                b = f1.readlines()
                total_R = 0.0
                total_P = 0.0
                total_F = 0.0
                for i in range(0, len(a)):
                    pred = b[i]
                    ori = a[i]
                    print(i + 1, '\t', evaluate(pred, ori))
                    R, P, F = evaluate(pred, ori)
                    total_R += R
                    total_P += P
                    total_F += F
                    csv_write.writerow([R, P, F])
                csv_write.writerow("")
                csv_write.writerow(["total_recall", "total_precision", "total_F-measure"])
                total_R /= len(a)
                total_P /= len(a)
                total_F /= len(a)
                csv_write.writerow([total_R, total_P, total_F])
                print(len(a) + 1, '\t', (total_P, total_R, total_F))
    # print(evaluate(pred_1,ori))
    # print(evaluate(pred_2,ori))