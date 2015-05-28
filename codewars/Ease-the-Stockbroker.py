# coding: utf-8

# coding: utf-8

import re

from math import ceil

def balance_statement(lst):
    stocks = re.split(r',\s+', lst)
    bad_formed = []
    pattern = re.compile(r'^([^\s]+)\s*(\d+)\s*(\d*\.\d+)\s*([BS])$')
    b_amount, s_amount = 0, 0
    for stock in stocks:
        if re.match(pattern, stock):
            print stock
            match = re.match(pattern, stock)
            name, quant, price, bs = match.group(1), match.group(2), match.group(3), match.group(4)
            amount = int(quant) * float(price)
            if bs == 'B':
                b_amount += amount
            else:
                s_amount += amount
        elif not stock:
            continue
        else:
            bad_formed.append(stock)
    b_cnt=len(bad_formed)
    b_amount = int(round(b_amount, 0))
    s_amount = int(round(s_amount, 0))


    if b_cnt >0:
        bad = "; Badly formed {b_cnt}: {b_string} ;".format(b_cnt=b_cnt, b_string=' ;'.join(bad_formed))
    else:
        bad = ''
    return "Buy: {b} Sell: {s}{bad}".format(b=b_amount, s=s_amount, bad=bad )


 # description: problem
 '''
Clients place orders to a stockbroker as strings.

The order can be simple or multiple.

Type of a simple order:

Quote /space/ Quantity /space/ Price /space/ Status

where

Quote is formed of non-whitespace character,
Quantity is an int,
Price a double (with mandatory decimal point "." ),
Status is B or S
B (buy) or the letter S (sell).

Example: "GOOG 300 542.0 B"

A multiple order is the concatenation of simple orders with a comma between each.

Example:
ZNGA 1300 2.66 B,
CLH15.NYM 50 56.32 B,
OWW 1000 11.623 B,
OGG 20 580.1 B"

To ease the stockbroker your task is to produce a string of type "Buy: b Sell: s" where b and s are 'double' formatted with no decimal (rounded to integers), b representing the total price of bought stocks and s the total price of sold stocks.

Example: "Buy: 294990 Sell: 0"

Unfortunately sometimes clients make mistakes. >>>
When you find mistakes in orders, you must pinpoint these badly formed orders
and produce a string of type:

"Buy: b Sell: s; Badly formed nb: badly-formed 1st simple order ;badly-formed nth simple order ;"

where nb is the number of badly formed simple orders, b representing the total price of bought stocks with correct simple order and s the total price of sold stocks with correct simple order.

Examples:

"Buy: 263 Sell: 11802; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;"
"Buy: 100 Sell: 56041; Badly formed 1: ZNGA 1300 2.66 ;"

'''

import re

def balance_statement(lst):
    stocks = re.split(r',\s+', lst)
    bad_formed = []
    pattern = re.compile(r'^([A-Z]+)\s*(\d+)\s*(\d+\.\d+)\s*([BS])$')
    for stock in stocks:
        if re.match(pattern, stock):
            print stock
    return "?"

balance_statement("ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B")



Oh dear!  balance_statement("GOOG 300 542.0 B, AAPL 50 145.0 B, CSCO 250.0 29 B, GOOG 200 580.0 S") returned:

'Buy: 169850 Sell: 116000;Badly formed 1: CSCO 250.0 29 B' should equal
'Buy: 169850 Sell: 116000; Badly formed 1: CSCO 250.0 29 B ;'
5


Oh dear!  balance_statement("GOOG 300 542.0 B, AAPL 50 145.0 B, CSCO 250.0 29 B, GOOG 200 580.0 S") returned:
'Buy: 169850 Sell: 116000; Badly formed 1: CSCO 250.0 29 B' should equal
'Buy: 169850 Sell: 116000; Badly formed 1: CSCO 250.0 29 B ;'



Oh dear!  balance_statement("CAP 1300 .2 B, CLH16.NYM 50 56 S, OWW 1000 11 S, OGG 20 580.1 S") returned:

'Buy: 0 Sell: 11602; Badly formed 3: CAP 1300 .2 B;CLH16.NYM 50 56 S;OWW 1000 11 S ;' should equal
'Buy: 260 Sell: 11602; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;'


CAP 1300 .2 B
OGG 20 580.1 S
Oh dear!  balance_statement("CAP 1300 .2 B, CLH16.NYM 50 56 S, OWW 1000 11 S, OGG 20 580.1 S") returned:
'Buy: 260 Sell: 11602; Badly formed 2: CLH16.NYM 50 56 S;OWW 1000 11 S ;'
'Buy: 260 Sell: 11602; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;'


Oh dear!  balance_statement("GOOG 4246.42 32.738 C, CAP 627 65 S, CITI 4223 9.75 S") returned:

'Buy: 0 Sell: 41175; Badly formed 2: GOOG 4246.42 32.738 C ;CAP 627 65 S ;'
'Buy: 0 Sell: 41174; Badly formed 2: GOOG 4246.42 32.738 C ;CAP 627 65 S ;'