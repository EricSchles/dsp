[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>

**Problem** : Quantifying the difference between total weight in pounds and pregnancy length using Cohen's d between first babies and other babies.

**How I solved it** : I imported the data from nsfg and the Cohen's *d* function from thinkstats2. I then quantified the difference between the total weight in lbs. From there, I calculated the pregnancy length and also applied the Cohen's *d* calculation to quantify the difference between pregnancy lengths.

**Solution** :

```python
import nsfg
import thinkstats2

#Finding the Cohen D calculation for difference in weight
baby_data = nsfg.ReadFemPreg()
nsfg.CleanFemPreg(baby_data)

first_baby_lbs = baby_data['totalwgt_lb'][baby_data.birthord == 1]
other_baby_lbs = baby_data['totalwgt_lb'][baby_data.birthord > 1]

print (("Cohen's D solution for lbs : ") + str(thinkstats2.CohenEffectSize(first_baby_lbs,other_baby_lbs)))

#Calculating Cohen's D for prglngth
first_baby_prglngth = baby_data['prglngth'][baby_data.birthord == 1]
other_baby_prglngth = baby_data['prglngth'][baby_data.birthord > 1]

print (("Cohen's D solution for prglength : ") + str(thinkstats2.CohenEffectSize(first_baby_prglngth,other_baby_prglngth)))

```

**Discussion** :

The Cohen's D solution for lbs is approx. 0.089 and the Cohen's D solution for prglength is approx. 0.029. Both are relatively low, which suggests that the they both factors have a low effect.