from collections import namedtuple

from dataclasses import dataclass

Transaction = namedtuple('Transaction', ['sender', 'receiver', 'amount', 'date'])

record = Transaction(sender='Jasim', receiver='Jewel Mahmud', amount='1000tk', date='2-08-20' )

print(record)
print(record.receiver, end=' ')
print(record.sender, end=' ')
print(record.amount, end=' ')
print(record.date, end=' ')
print('\n')

print(record[0], '\n')
print(record[1], '\n')


@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float
    date: str


record1 = Transaction(sender='Shanto', receiver='Reyadul', amount=10000.0, date='02-06-20')

print(record1.amount)
print(record1.receiver)
# print(record1[0]) is not possible in dataclasses


"""
NamedTuple behaves like a tuple, while DataClass behaves more like a regular Python class because by default, 
the attributes are all mutable and they can only be accessed by name, not by index
"""