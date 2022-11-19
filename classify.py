import json
import pandas as pd

origin_data = pd.read_csv('res.csv')

type2name = {1: "计算机体系结构/并行与分布计算/存储系统",
            2: "计算机网络",
            3: "网络与信息安全",
            4: "软件工程/系统软件/程序设计语言",
            5: "数据库/数据挖掘/内容检索",
            6: "计算机科学理论",
            7: "计算机图形学与多媒体",
            8: "人工智能",
            9: "人机交互与普适计算",
            10: "交叉/综合/新兴"}

data = pd.read_excel("./CCF_Map.xlsx")
data['领域'] = data['类别'].apply(lambda x: type2name[x])
data = data[['刊物全称','等级','领域']]

def handle_err(i, j):
    try:
        return (data.loc[j, '刊物全称'].lower() in origin_data.loc[i, 'raw'].lower())
    except:
        return False

full_name = [None] * len(origin_data)
rank = [None] * len(origin_data)
area = [None] * len(origin_data)
for i in range(len(origin_data)):
    for j in range(len(data)):
        if handle_err(i, j):
            print(i,j)
            full_name[i] = data.loc[j, '刊物全称']
            rank[i] = data.loc[j, '等级']
            area[i] = data.loc[j, '领域']
            break
origin_data['full_name'] = full_name
origin_data['rank'] = rank
origin_data['area'] = area

origin_data.to_csv('test.csv', index=False)

df = pd.read_csv('test.csv')