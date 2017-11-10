""" BETTER WAY 30: Use @property in refactoring -PART.2- """
import datetime
# from datetime import datetime

SEPARATOR = '\n' + '__'*20 + '\n'


class Bucket(object):
    def __init__(self, period):
        self.period_delta =  datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.max_quota = 0          # changed
        self.quota_consumed = 0     # changed

    def __repr__(self):
        return 'Bucket(max_quota= %d, quota_consumed= %d)' %(
                                        self.max_quota,
                                        self.quota_consumed)
    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount

        if amount == 0:
            """ reset quota of new period """
            self.quota_consumed = 0
            self.max_quota = 0

        elif delta < 0:
            """ fill quota of new period """
            assert self.quota_consumed == 0
            self.max_quota = amount

        else:
            """ consum quota of new period """
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


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

def show_now(bucket):
    print('Initial =', bucket, SEPARATOR)

def show_status_fill(bucket, amount):
    fill(bucket, amount)
    print('... Fill %s quota in Bucket ...' %amount)
    print(bk, SEPARATOR)

def show_status_deduct(bucket, amount):
    if deduct(bucket, amount):
        print('... Had %s quota from Bucket ...' %amount)
    else:
        print('\t*** ERROR ***\n')
        print('... Sorry, Not enough for %s quota ...' %amount)
    print(bucket, SEPARATOR)

bk = Bucket(60)

show_now(bk)

show_status_fill(bk, 100)
show_now(bk)

show_status_deduct(bk, 99)
show_now(bk)

show_status_deduct(bk, 3)
show_now(bk)
