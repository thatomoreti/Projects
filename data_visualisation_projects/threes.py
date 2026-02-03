import matplotlib.pyplot as plt
plt.style.available
import seaborn

threes=[3,6,9,12,15,18]
squares=[1,2,4,9,16,25]

plt.style.use('ggplot')
fig , ax = plt.subplots()



ax.plot(threes,squares,linewidth=1)
# px.plot(squares)


ax.set_title("Square Numbers and Pattern of threes", fontsize=24)
ax.set_xlabel("Threes", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)

ax.tick_params(axis='both', labelsize=12)

ax.set_xticks(threes)
ax.set_yticks(squares)

plt.show()