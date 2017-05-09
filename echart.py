'''from echarts import Echart, Legend, Pie
chart = Echart(u'徐孝天微信好友性别比例' )
chart.use(Pie('WeChat', 
    [{'value': '0.4812', 'name': u'男性 %.2f%%' % (48.12)},
    {'value': '0.5001', 'name': u'女性 %.2f%%' % (50.01)},
    {'value': '0.1870', 'name': u'其他 %.2f%%' % (1.87)}],
    radius=["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
chart.plot()

from echarts import Echart, Legend, Bar, Axis

chart = Echart('GDP', 'This is a fake chart')
chart.use(Bar('China', [2, 3, 4, 5]))
chart.use(Legend(['GDP']))
chart.use(Axis('category', 'bottom', data=['Nov', 'Dec', 'Jan', 'Feb']))
chart.plot()
'''
import matplotlib.pyplot as plt
 
# Data to plot
labels = ['male', 'female', 'Unknown']
sizes = [368, 460, 42]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
