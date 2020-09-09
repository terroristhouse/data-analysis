import pandas as pd
from dateutil.parser import *
import warnings
warnings.filterwarnings('ignore')

"""获取数据"""
df = pd.read_csv('crime_data_20200424.csv')
# print(df.head())

"""统计犯罪类型出现的次数前十个，绘图为横向条形图"""
# print(df.crime.value_counts().iloc[:10])
# ax = df.crime.value_counts().iloc[:10].sort_values().plot.barh()
# fig = ax.get_figure()
# fig.savefig('犯罪类型前十.png',bbox_inches='tight')

"""提取抢劫类型的犯罪"""
robbery = df[df.crime.str.contains('ROBBERY')]
# print(robbery.head())
# print(robbery.shape)
# """查看犯罪位置，以及每种类型对应的记录条目数"""
# print(robbery.groupby('locname').size().sort_values(ascending=False))
# """结果可视化"""
# ax = robbery.groupby('locname').size().sort_values(ascending=False).head(10).sort_values().plot.barh()
# fig = ax.get_figure()
# fig.savefig('入室抢劫犯罪地点.png',bbox_inches='tight')

"""研究哪些街区比较危险"""
# regex = r"\d+XX\s(?P<street>.*)"
# subst = "\\g<street>"
# robbery["street"] = robbery.publicadress.str.replace(regex, subst)
# print(robbery.groupby('street').size().sort_values(ascending=False).head(10))
# ax = robbery.groupby('street').size().sort_values(ascending=False).head(10).sort_values().plot.barh()
# fig = ax.get_figure()
# fig.savefig('危险街区.png',bbox_inches='tight')

"""利用时间数据进行切分"""
robbery["year"] = robbery.incidentdatetime.apply(lambda x: parse(x).year)
robbery["month"] = robbery.incidentdatetime.apply(lambda x: parse(x).month)
robbery["hour"] = robbery.incidentdatetime.apply(lambda x: parse(x).hour)
# print(robbery.groupby('year').size())
# ax = robbery.groupby('year').size().plot()
# fig = ax.get_figure()
# fig.savefig('以年份统计.png')

"""比较一下，不同月份之间，是否有明显的抢劫犯罪发生数量差别。"""
# print(robbery.groupby('month').size())
# ax = robbery.groupby('month').size().plot.bar()
# # ax = robbery[robbery.year == 2019].groupby('month').size().plot.bar()
# fig = ax.get_figure()
# fig.savefig('以月份统计.png')


"""抢劫一般发生在什么时间。这次我们用的，是小时（hour）数据。"""
# ax = robbery.groupby('hour').size().plot.bar()
# fig = ax.get_figure()
# fig.savefig('以小时统计.png')

"""看看2019年的情况"""
ax = robbery[robbery.year == 2019].groupby('hour').size().plot.bar()
fig = ax.get_figure()
fig.savefig('2019年按小时统计.png')

