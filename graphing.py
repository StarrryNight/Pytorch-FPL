import matplotlib.pyplot as plot
import seaborn as sns
class graphing():
    def graph(x,y):
        sns.scatterplot(x=x,y=y)
        plot.show()