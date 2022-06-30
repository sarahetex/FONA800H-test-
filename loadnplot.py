import pandas
import matplotlib.pyplot as plt
dataset = pandas.read_csv('World Energy Consumption.csv', usecols=[1], engine='python')
plt.plot(dataset)
plt.show()
#this code to load and plot the dataset
# much have a two vector data set

#The Long Short-Term Memory network, or LSTM network, is a recurrent neural network that is trained using Backpropagation Through Time and overcomes the vanishing gradient problem.
