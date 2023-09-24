import matplotlib.pyplot as plt

left = [1,2,3,4,5]
height = [138,35,10,5,147]
tick_label = ['Accenture', 'Spplus', 'Tejas', 'L&T','Amazon']
plt.bar(left, height, tick_label = tick_label, width = 0.5, color = ['blue', 'Red'])
#plt.plot(x,y, color ='pink', linestyle = 'dashed', linewidth = 3, marker='o', markerfacecolor = 'blue', markersize=9)
#plt.ylim(1,8)
#plt.xlim(1,8)
#plt.plot(x,y)
plt.xlabel('Listed Companies')
plt.ylabel('Stock price')
plt.title('Project - Companies Stock prices')
plt.show() 
 