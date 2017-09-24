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

    write(exchange, {"type": "add", "order_id": 1, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 20})

    write(exchange, {"type": "add", "order_id": 2, "symbol": "BOND", "dir": "SELL", "price": 1002, "size": 20})

    write(exchange, {"type": "add", "order_id": 3, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 40})

    write(exchange, {"type": "add", "order_id": 4, "symbol": "BOND", "dir": "SELL", "price": 1002, "size": 40})

    write(exchange, {"type": "add", "order_id": 5, "symbol": "BOND", "dir": "BUY", "price": 999, "size": 20})

    write(exchange, {"type": "add", "order_id": 6, "symbol": "BOND", "dir": "SELL", "price": 1002, "size": 20})






    #Trading for stocks:
    #Goldman Sachs keeps falling so do not buy
    #Morgan Stanley is staying steadily, so I'll invest:

    #Exchange runs:
    print("The exchange replied:", hello_from_exchange, file=sys.stderr)
    while (True):
        exch_msg = read(exchange)
        print("Exchange:", exch_msg, file=sys.stderr)

if __name__ == "__main__":
    main()
