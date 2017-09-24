#!/usr/bin/python
from __future__ import print_function

import sys
import socket
import json

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("production", 25000))
    return s.makefile('rw', 1)

def write(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")

def read(exchange):
    return json.loads(exchange.readline())

def main():
    exchange = connect()

    write(exchange, {"type": "hello", "team": "TANIS"})
    hello_from_exchange = read(exchange)


    #Algorithms:

    #Algorithm for Bonds:
    #Bonds are the safest, so buy low and sell high:
    #Default price is 1000, so try to make some profit on bonds:
    #990 is buy price and 1002 is sell price.

    amountOfBondsPurchased = 5

    bondAddID = 0

    for bondAddID in range(0,1):
        write(exchange, {"type": "add", "order_id": bondAddID, "symbol": "BOND", "dir": "BUY", "price": 998, "size": 50})

    amountOfBoundsSold = 6

    bondSellID = 1

    for boundSellID in range(2,3):
        write(exchange, {"type": "add", "order_id": bondSellID, "symbol": "BOND", "dir": "SELL", "price": 1002, "size": 50})

    #Trading for stocks:
    #Goldman Sachs keeps falling so do not buy
    #Morgan Stanley is staying steadily, so I'll invest:

    MSID = 7

    for MSID in range(7, 12):
        write(exchange, {"type": "add", "order_id": MSID, "symbol": "MS", "dir": "BUY", "price": 4000 , "size": 1})
        write(exchange, {"type": "add", "order_id": MSID, "symbol": "MS", "dir": "BUY", "price": 4500 , "size": 1})

    #Exchange runs:
    print("The exchange replied:", hello_from_exchange, file=sys.stderr)
    while (True):
        exch_msg = read(exchange)
        print("Exchange:", exch_msg, file=sys.stderr)

if __name__ == "__main__":
    main()
