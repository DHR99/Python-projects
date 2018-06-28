# Loading libraries
import time
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from matplotlib.animation import FuncAnimation


filename = 'NB_results.pkl' # loading pickle file
NB_results = pickle.load(open(filename, 'rb'))
NB_results = NB_results.iloc[4:, :] # first were neutral for both candidates


# initializing the counters
positive_petro = 0
positive_duque = 0


for name, sent in zip(NB_results.tweet, NB_results.sentiment):
    # time margin of 2-3 seconds between tweets
    wait = np.random.normal(3.5, 2.5) 
    if wait < 0:
        wait = 0
    # Wait for 5 seconds
    time.sleep(wait)
    # conditions: if positive and @X then the tweets is positive toward that candidate(@X)
    if '@petrogustavo' in name[0] and sent == 'P':
        positive_petro += 1
    elif '@IvanDuque' in name[0] and sent == 'P':
        positive_duque += 1
    clear_output()
    
    print('Positive tweets for Petro: ', positive_petro)
    print('Positive tweets for Ivan: ', positive_duque)
    print('------------------------------------------------')
    print(name[0])
    print('------------------------------------------------')
    print('PREDICTION:')
    
    
    # conditions to check who is winning
    if positive_petro > positive_duque:
        print('Petro is winning')
    elif positive_petro < positive_duque:
        print('Ivan is winning')
    else:
        print('Battle!!!') 

    colors = ['blue', 'red']
    
    labels = ['PetroGustavo', 'IvanDuque']
    nums = [positive_petro, positive_duque]
    
    def update(num):
        """ Function to update at each frame the pie chart"""
        ax.clear()
        ax.axis('equal')
        str_num = str(num)
        for x in range(2):
            nums[x] += str_num.count(str(x))
        ax.pie(nums, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax.set_title(str_num)

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update, frames=range(10000), repeat=False)
    plt.show()
    
    print('========================================================')
    print('========================================================')