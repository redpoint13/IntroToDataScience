import numpy as np
import scipy.stats
import pandas as pd

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file by downloading the baseball_stats file from Downloadables below. 
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """
    df = pd.read_csv(filename)
    df_r = df[df.handedness=='R'] # breaks out only the righties
    # print df_r
    df_l = df[df.handedness=='L'] # breaks out only the lefties
    
    t_stat = scipy.stats.ttest_ind(df_r['avg'], df_l['avg'], equal_var = False)
    
    # A P-value can also be reported more formally in terms of a fixed level alpha test. 
    # Here alpha is a number selected independently of the data, usually 0.05 or 0.01, 
    # more rarely 0.10. We reject the null hypothesis at level alpha if the P-value is 
    # smaller than alpha, otherwise we fail to reject the null hypothesis at level alpha.
    # http://www.stat.ualberta.ca/~hooper/teaching/misc/Pvalue.pdf
   
    alpha = .05
    if ( t_stat.pvalue < alpha ):
        return (False, t_stat)
    else:
        return (True, t_stat)
    #print t_stat.pvalue
    
filename = 'C:/Users/Tony/Documents/GitHub/IntroDataScience/lesson3/baseball_stats.csv'
result = compare_averages(filename)
print result