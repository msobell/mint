#! /usr/bin/env python
"""
Usage: %s <number N>

Solves the Mint problem (http://cs.nyu.edu/courses/fall10/G22.2965-001/mint.html)
"""
import os
import sys
import time

start_time = time.time()
#lt = {}

class wereDone(Exception):
    pass

def usage():
    sys.stdout.write( __doc__ % os.path.basename(sys.argv[0]))

try:
    N = sys.argv[1]
except:
    usage()
    sys.exit(1)

def score_coins(t):
    for i in range(1,100):
        if i % 5 == 0:
            t[i] *= int(N)
    return sum(t[1:100])

# PROBLEM 1
def find_exact_change_values(coins):
    a = [100]*101

    # exact change number for each coin is 0
    for coin in coins:
        a[coin] = 0

    # and 0 is 0
    a[0] = 0

    for i in range(1,101):
        tries = [100]*5 #one try for each coin
        j = 0
        for coin in coins:
            if (i >= coin):
                tries[j] = a[i-coin] + 1
                j=j+1        
        a[i] = min(tries) #best coin scenario
    return a

# PROBLEM 2
def find_exchange_values(coins, b):
    # return array ex. 43 thru 50
    # add to exact change number of the difference
    b[0] = 0
    b[100] = 0
    c = [100]*101 #0 to 100
    for amt in range(0,51):
        tries = [100]*101
        for j in range(amt,101):
#            print "b["+repr(j)+"]: " + repr(b[j]) + "\t" + repr(b[j-amt])
            tries[j] = b[j] + b[ j - amt ]
        c[amt] = c[100-amt] = min(tries)
    c[100] = 0
    return c

#PROBLEM 2
def find_coins():
    coins = [1]*5

    print "Minting..."
    
    exact_change_min = 100*100
    exchange_min = 100*100
    t = []
    good_coins = [1]*5
    limit = 50
    for i in range(5,limit):
        if time.time() - start_time > 120:
            print "Whoops, out of time!"
            print "Exact Change Coins:\t" + repr(exact_change_coins) + "\t Score: " + repr(exact_change_min)
            print "Exchange Coins:\t\t" + repr(exchange_coins) + "\t Score: " + repr(exchange_min)
            sys.exit(2)
        print repr(i)+"\t"+repr(int(time.time() - start_time)) + " seconds"
        for j in range(4,limit-10):
            for k in range(3,limit-25):
                for l in range(2,limit-40):
                    if l < k < j < i:
                        coins = [1,l,k,j,i]
                        exact_change = find_exact_change_values(coins)
                        exact_change_score = score_coins(exact_change)
                        if exact_change_min > exact_change_score:
                            exact_change_min = exact_change_score
                            print "Exact change min:\t" + repr(exact_change_min)
                            exact_change_coins = coins
                        
                        exchange = find_exchange_values(coins, exact_change)
                        exchange_score = score_coins(exchange)
                        if exchange_min > exchange_score:
                            exchange_min = exchange_score
                            print "Exchange min:\t\t" + repr(exchange_min)
                            exchange_coins = coins
                        
    print ""
    print "Exact Change Coins:\t" + repr(exact_change_coins) + "\t Score: " + repr(exact_change_min)
    print "Exchange Coins:\t\t" + repr(exchange_coins) + "\t Score: " + repr(exchange_min)

    try:
        print repr(int(time.time() - start_time)) + " seconds"
    except:
        pass
    print ""

if __name__ == "__main__":

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    N = sys.argv[1]
    print "Solving for " + N

    find_coins()
