from cmath import nan
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import math


plt.rcParams['font.sans-serif'] = ['SimHei']
map = {"计算机网络": "Network",  "软件工程/系统软件/程序设计语言": "Software", "网络与信息安全": "Security", "人工智能": "AI", "计算机体系结构/并行与分布计算/存储系统": "System",
"数据库/数据挖掘/内容检索": "Database", "计算机图形学与多媒体": "Media", "交叉/综合/新兴": "X", "人机交互与普适计算": "Interaction", "计算机科学理论": "Theory"}

def plot_pie(df, paras):
    df.plot(
        kind='pie',
        title=paras['title'],
        autopct='%.1f%%',
        xlabel = None
    )


def plot_select(df, type_abc, sort_list):
    _df = df[df['rank']==type_abc]['area'].value_counts()
    _df = _df.reindex(index=sort_list)
    _df = _df.fillna(0)
    _df.name = None
    print(_df)
    paras = {
        'title': '%s类分布'%type_abc
    }
    plot_pie(_df, paras)

def handle_nan(map, key):
    try:
        return map[key]
    except:
        return None

def main():
    # 读取数据
    df = pd.read_csv('test.csv')
    df['area'] = df['area'].apply(lambda x: handle_nan(map, x))
    # 总体
    _df = df['area'].value_counts()
    sort_list = _df.index
    _df.name = None
    print(_df)
    paras = {
        'title': '总体分布'
    }
    plot_pie(_df, paras)
    plt.show()

    plt.figure()
    # A
    ax1 = plt.subplot(1,3,1)
    plt.sca(ax1)
    plot_select(df, 'A', sort_list)
    # B
    ax2 = plt.subplot(1,3,2)
    plt.sca(ax2)
    plot_select(df, 'B', sort_list)
    # C
    ax3 = plt.subplot(1,3,3)
    plt.sca(ax3)
    plot_select(df, 'C', sort_list)
    plt.show()

def handle_str(x):
    try:
        return [i for i in x.replace('\'','').split(']')[0].split('[')[1].split(',')]
    except:
        return None


def show_wordcloud():
    df = pd.read_csv('test.csv')

    words = []
    for x in df['keywords'].values:
        items = handle_str(x)
        if items == None:
            continue
        for i in items:
            words.append(i)
    wcloud = WordCloud(width=2800, height=1600).generate(''.join(words))
    plt.imshow(wcloud)
    plt.axis('off')
    plt.show()

def show_all():
    df = pd.read_csv('test_1022.csv')
    ccf = [0,0,0,0,0,0]
    no_ccf = [0,0,0,0,0,0]

    x_axis_data = [2017,2018,2019,2020,2021,2022]

    for index, row in df.iterrows():
        if row['area'] in map:
            if row['year'] in x_axis_data:
                # dic[map[row['area']]][x_axis_data.index(row['year'])] += 1
                ccf[x_axis_data.index(row['year'])] += 1
        elif row['year'] in x_axis_data:
            no_ccf[x_axis_data.index(row['year'])] += 1

    all_ccf = [i + j for i, j in zip(ccf, no_ccf)]

    #画图 
    plt.plot(x_axis_data, ccf, 'b*--', alpha=0.5, linewidth=1, label='ccf')#'
    plt.plot(x_axis_data, no_ccf, 'rs--', alpha=0.5, linewidth=1, label='not_ccf')
    plt.plot(x_axis_data, all_ccf, 'go--', alpha=0.5, linewidth=1, label='all')

    plt.title("Smart contract papers from 2017 to 2022")
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('number')
    
    plt.show()

def ccf(rank = None):
    df = pd.read_csv('test_1022.csv')
    # 替换A/B/C
    if rank != None:
        df = df[df['rank']==rank]

    dic = {
        "Network": [0,0,0,0,0,0],
        "Software": [0,0,0,0,0,0],
        "Security": [0,0,0,0,0,0],
        "AI": [0,0,0,0,0,0],
        "System": [0,0,0,0,0,0],
        "Database": [0,0,0,0,0,0],
        "Media": [0,0,0,0,0,0],
        "X": [0,0,0,0,0,0],
        "Interaction": [0,0,0,0,0,0],
        "Theory": [0,0,0,0,0,0]
    }

    x_axis_data = [2017,2018,2019,2020,2021,2022]

    for index, row in df.iterrows():
        if row['area'] in map:
            if row['year'] in x_axis_data:
                dic[map[row['area']]][x_axis_data.index(row['year'])] += 1

    for i in dic.keys():
        print(i)
        if i == "Network":
            plt.plot(x_axis_data, dic[i], 'b*-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "Software":
            plt.plot(x_axis_data, dic[i], 'rs-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "AI":
            plt.plot(x_axis_data, dic[i], 'go-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "Security":
            plt.plot(x_axis_data, dic[i], 'mv-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "System":
            plt.plot(x_axis_data, dic[i], 'yd-', alpha=0.5, linewidth=1, label=i)
            continue
        else:
            plt.plot(x_axis_data, dic[i], '--', alpha=0.5, linewidth=1, label=i)

    if rank != None:
        plt.title("Smart contract papers classified by CCF " + rank + " from 2017 to 2022")
    else:
        plt.title("Smart contract papers classified by CCF from 2017 to 2022")
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('number')
    
    plt.show()


def tech_class():
    df = pd.read_csv('test_1022.csv')
    df = df.fillna('')
    x_axis_data = [2017,2018,2019,2020,2021,2022]
    dic = {"abstract interpretation": [0,0,0,0,0,0], "symbolic execution": [0,0,0,0,0,0], "fuzzing": [0,0,0,0,0,0], "formal verification": [0,0,0,0,0,0], "machine learning": [0,0,0,0,0,0], "model checking": [0,0,0,0,0,0], "concolic": [0,0,0,0,0,0]}
    for index, row in df.iterrows():
        content = ''
        content = content + row["title"] + row["pubAbstract"] + row["keywords"]
        for key in dic:
            if key in content:
                if row['year'] in x_axis_data:
                    dic[key][x_axis_data.index(row['year'])] += 1
                    continue
    
    for i in dic.keys():
        print(i)
        if i == "abstract interpretation":
            plt.plot(x_axis_data, dic[i], 'b*-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "symbolic execution":
            plt.plot(x_axis_data, dic[i], 'rs-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "fuzzing":
            plt.plot(x_axis_data, dic[i], 'go-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "formal verification":
            plt.plot(x_axis_data, dic[i], 'mv-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "machine learning":
            plt.plot(x_axis_data, dic[i], 'yd-', alpha=0.5, linewidth=1, label=i)
            continue
        elif i == "model checking":
            plt.plot(x_axis_data, dic[i], 'yD-', alpha=0.5, linewidth=1, label=i)
            continue
        else:
            plt.plot(x_axis_data, dic[i], '--', alpha=0.5, linewidth=1, label="concolic testing")
    
    plt.title("Smart contract techniques trend from 2017 to 2022")
    plt.legend()
    plt.xlabel('year')
    plt.ylabel('number')
    
    plt.show()


# ccf()

tech_class()
# show_all()