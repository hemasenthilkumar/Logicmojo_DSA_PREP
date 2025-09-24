"""
Rabin Karp algorithm

instead of checking every character, we can create a hash using a hash value
h1 = txt eg. abc = 97+98+99
h2 = pat eg. abe = some value

The inner loop where we do the comparision -> will run only if the hashes match h1=h2

sometimes the hash values might be same for many things
we have to select a unique hash function

txt = a b c d e f g h i a b e 
eg h1(bcd) = h1(abc) - h1(a) + h1(d) --> we remove the prev value and add the new one
this can be done in constant time, instead of calculating for all

The rabin karp algorithm to do this is:

hash = hash + char * q ^ i
where q = prime number and i is the index

lets say q = 3
Eg. h2 of abe = 98 * 3 + 99 * 3^2 + 101 * 3^3 = some X

for next sequence h2 
= (h2 - a) # remove out of the window
= h2 / q

For eg:
lets say h2 = a * 3 + b * 3^2 + c * 3^3
h2-a means = 3 + b * 3^2 + c * 3^3
then h2/q = 1 + b * 3 + c * 3^2
h2 + new char =  b*3 + e*3^2 + d*3^3
"""