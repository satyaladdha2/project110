import pandas as pd
import statistics
import csv 
import plotly.figure_factory as ff
import random 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

dataset=[]

for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation = statistics.stdev(dataset)
print("mean of sample:", mean )
print( "std_deviation of sample: ",std_deviation)


population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("population_mean:" , population_mean)
print("std_deviation:" , std_deviation)

def show_fig(mean_list):    
    df = mean_list
    fig = ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines" , name = "MEAN"))
    fig.show()
