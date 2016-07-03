[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>

**Problem** : I have to determine how to solve the percentage of men who are eligible to join the Blue Man Group in the United States.

**How I solved it** : Since the information provided was inconsistent, I first created a function that could convert the height from inches to centimeters. I then took the CDF of the lower limit and subtracted that from the CDF of the upper limit. To calculate the CDF of the normal distributions, I used the scipy package.

**Solution** :

```python

import scipy.stats

%matplotlib inline

# Mean
mu = 178
# Standard Deviation
sigma = 7.7

def convert_height(height_inch):
    height_cm = height_inch * 2.54
    return height_cm

lower_limit = convert_height(70)
upper_limit = convert_height(73)

lower_limit_cdf = scipy.stats.norm.cdf(lower_limit, loc=mu, scale=sigma)
upper_limit_cdf = scipy.stats.norm.cdf(upper_limit, loc=mu, scale=sigma)

print (float (upper_limit_cdf - lower_limit_cdf) * 100)

```

**Discussion** : Approximately 34.27% of men in the United States are eligible to join the Blue Man Group.

