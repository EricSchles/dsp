[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>

**Problem** : For this exercise, I plotted the actual and biased distributions in regards to the number of children in the household. By plotting the two, I can magnify the bias that exists when we ask children who have households with many children.

**How I solved it** : I decided to use the author's Pmf function to do a majority of the calculations and thinkplot for plotting the actual vs bias data. I then created a copy of the original data and placed a bias on it.

**Solution** :

```python
# enabling plots to be displayed in jupyter / importing data
%matplotlib inline

import chap01soln
import thinkstats2
import thinkplot

data = chap01soln.ReadFemResp()

# calculating the pmf data for number of kids in the household
pmf = thinkstats2.Pmf(resp.numkdhh)

# Copying data import and placing bias on it

biased = pmf.Copy(label='biased')

for x, p in pmf.Items():
    biased.Mult(x, x)

biased.Normalize()

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()
```

![Solution to 3.1](https://github.com/floofydugong/dsp/blob/master/ThinkStats2/code/Solution_for_3_1.png)

**Discussion** :

The normal_pmf mean was  1.02420515504 while the the bias_pmf mean was 2.40367910066.

As one can see, the plots do confirm that children belonging to households with multiple children exemplify the "class size paradox", pushing the mean higher by approximately 1.4.