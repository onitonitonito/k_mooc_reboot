""" BETTER WAY 30: Use @property in refactoring """
import datetime
# from datetime import datetime

SEPARATOR = '\n' + '__'*20 + '\n'

class Bucket(object):
    def __init__(self, period):
        self.period_delta =  datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.quota = 0

    def __repr__(self):
        return 'Bucket(quota= %d)' %self.quota


def fill(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

def deduct(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True

def show_status_deduct(bucket, amount):
    if deduct(bucket, amount):
        print('... Had %s quota from Bucket ...' %amount)
    else:
        print('\t*** ERROR ***\n')
        print('... Sorry, Not enough for %s quota ...' %amount)
    print(bucket, SEPARATOR)

def show_status_fill(bucket, amount):
    fill(bucket, amount)
    print('... Fill %s quota in Bucket ...' %amount)
    print(bk, SEPARATOR)

bk = Bucket(60)

fill(bk, 100)
print(bk, SEPARATOR)           # Bucket(quota= 100)

show_status_deduct(bk, 40)
show_status_fill(bk, 40)


if deduct(bk, 85):
    print('... Had 99 quota from Bucket ...')
else:
    print('\t*** ERROR ***\n')
    print('... Sorry, Not enough for 99 quota ...')
print(bk, SEPARATOR)

if deduct(bk, 20):
    print('... Had 3 quota  from Bucket ...')
else:
    print('\t*** ERROR ***\n')
    print('... Sorry, Not enough for 3 quota ...')
print(bk, SEPARATOR)
