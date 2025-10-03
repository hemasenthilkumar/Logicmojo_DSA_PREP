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

For eg: if i = 1
lets say h2 = a * 3 + b * 3^2 + c * 3^3
h2-a means = 3 + b * 3^2 + c * 3^3
then h2/q = 1 + b * 3 + c * 3^2
h2 + new char =  b*3 + e*3^2 + d*3^3

lets do for
h1 = abcdefghiabe
h2 = abe

i= 0

h2(abe) = 97 * 1 + 98 * 3 + 101 * 9 = 1300

h1(abc) = 97 * 1 + 98 * 3^1 + 99 * 3^2 = 1282
for now moving a out and adding d we have to:

h1(bcd) = (h1(abc) - a) / 3 + d * 9
        = 395 + 100 * 9
        = 1295

we have to check if the hash of abe is matching abc or bcd then only we start
the comparision

"""

def searchPattern(txt, pat):
        n, m = len(txt), len(pat)
        d = 256        # alphabet size
        q = 101        # a prime modulus
        res = []

        # h = d^(m-1) % q
        h = pow(d, m-1, q)

        # initial hash values
        p, t = 0, 0
        for i in range(m):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q

        # slide over text
        for i in range(n - m + 1):
            if p == t:  # potential match
                if txt[i:i+m] == pat:
                    res.append(i)

            if i < n - m:
                t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q
                if t < 0:  # handle negative values
                    t += q

        return res


if __name__ =="__main__":
    txt = "abcab"
    pat = "ab"
    print(searchPattern(txt, pat))