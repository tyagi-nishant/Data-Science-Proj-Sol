
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[1]:

import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')


# In[2]:

#creating subplots using gridspec functionality
import matplotlib.gridspec as gridspec

plt.figure()
gspec = gridspec.GridSpec(4, 4)

p1 = plt.subplot(gspec[0, 1:3])
p2 = plt.subplot(gspec[2, 2:4])
p3 = plt.subplot(gspec[3, 3:])


# In[3]:

fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
axs=[ax1,ax2,ax3,ax4]

X = np.random.random(size=10000)
axs[0].hist(x1, bins=10, normed=True,color='red')
axs[1].hist(x2, bins=100, normed=True,color='blue')
axs[2].hist(x3, bins=100, normed=True,color='green')
axs[3].hist(x4, bins=100, normed=True,color='yellow')



# In[4]:

import matplotlib.animation as animation

n = 30
x1 = np.random.randn(n)
x2 = np.random.randn(n)

# create the function that will do the plotting, where curr is the current frame
def update1(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr == n: 
        a.event_source.stop()
    plt.cla()

    bins = np.arange(-4, 4, 0.5)
    
    plt.hist(x1[:curr], bins=bins)
    
   
    plt.axis([-4,4,0,30])
    plt.gca().set_title('Sampling the Normal Distribution')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr), [3,27])
def update2(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr == n: 
        a.event_source.stop()
    plt.cla()

    bins = np.arange(-4, 4, 0.5)
    
    plt.hist(x2[:curr], bins=bins)
    
    plt.hist(x[:curr], bins=bins)
    plt.axis([-4,4,0,30])
    plt.gca().set_title('Sampling the Normal Distribution')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr), [3,27])


# In[5]:

fig = plt.figure()
plt.subplot(122)
a = animation.FuncAnimation(fig,update1, interval=100)
plt.subplot(121)
a = animation.FuncAnimation(fig,update2, interval=100)

