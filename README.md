# ASE
CSC791-Fall 2019_Automated Software Engineering Course

Name:Viviniya Alexis Lawrence
unity id: palexis

HW 1
Write a class called Col with subclass Num, Sym, and Some

In Num, write code that read a number one at a time, and incrementally update mean and standard deviation. For pseudocode on how to do that, see Num.

you'll only need down to code line 35.
Test your code:

build a list of 100 random numbers
add the list, one at a time to a Num
every ten numbers, cache the mean and standard deviation
i.e. that cache is two lists of means and standard deviations seen at "i" = 10,20,30, etc
now delete those numbers, one at a time, from that Num.
every ten numbers check that you are getting the same thing as the cache
For a sample of that code, in another language, see _num
Caution:

There is a known bug in the NumLess function of Num. Those sums go wrong when the sample is small and sum is small (due to some deep issues with the representation of reals... we won't be able to fix that).
So when deleting the numbers, run from 100 down to 10 then stop.
