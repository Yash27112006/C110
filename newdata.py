import csv
import random
import statistics
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("newdata.csv")
data = df["average"].tolist()

population_mean = statistics.mean(data)
std_dev =statistics.stdev(data)

fig = ff.create_distplot([data], ["average"])
fig.show()

print("population mean: ",population_mean)
print("standard deviation: ",std_dev)

def show_fig(mean_list):
    df=mean_list
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution: ", mean)
    fig = ff.create_distplot([df],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean],y=[0,12],mode="lines",name="MEAN"))
    fig.show()

dataset = []


#std_dev =statistics.stdev(dataset)

# print("sample mean: ",mean)
# print("sample standard deviation: ",std_dev)
# show_fig()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        rand_index = random.randint(0,len(data)-1)
        value = data[rand_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def std_deviation():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_dev = statistics.stdev(mean_list)
    print("standard deviation of the sampling distribution",std_dev)

setup()
std_deviation()

