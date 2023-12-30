# Email Scheduler
from datetime import datetime, timedelta
from Heap import Heapq
import heapq

def emailScheduler(frequency, details):
    current = datetime.now()
    while True:
        current += frequency
        yield current, details

def getTopK(k, data):
    return heapq.nsmallest(k, data.splitlines(), key=lambda x: -float(x.split()[-1]))

if __name__ == '__main__':
    email1 = emailScheduler(timedelta(minutes=15), "First email")
    email2 = emailScheduler(timedelta(minutes=40), "Second email")
    unified = heapq.merge(email1, email2)

    results = """\
    Christania Williams      11.80
    Marie-Josee Ta Lou       10.86
    Elaine Thompson          10.71
    Tori Bowie               10.83
    Shelly-Ann Fraser-Pryce  10.86
    English Gardner          10.94
    Michelle-Lee Ahye        10.92
    Dafne Schippers          10.90"""
    
    print('\n'.join(getTopK(3, results)))