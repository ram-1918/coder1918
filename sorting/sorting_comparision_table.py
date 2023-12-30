# Sorting Algorithms Execution time comparision
from bubblesort import bubblesort
from insertionsort import insertionsort
from selectionsort import selectionsort
from mergesort import mergesort_alg
from quicksort import quicksort_alg

import pandas as pd

if __name__ == '__main__':
    lst = [21, 43, 12, 23, 1, 3, 65, 0, 2, 3, 21,42,21,32,435,13,1,42,1,21,5,657,5,2315,45,213,1,53,56,4,424,2,64,875866,324,23,14,24,235,24,2,42,42,4,53,4,32,54,3,4,2,42,4,345,5,5,55545]
    d = {'Exec. Times': [bubblesort(lst)[1], insertionsort(lst)[1], selectionsort(lst)[1], mergesort_alg(lst)[1], quicksort_alg(lst)[1]]}
    table = pd.DataFrame(d, index=['Bubblesort', 'Insertionsort', 'Seletionsort', 'Mergesort', 'Quicksort'])
    table = table.sort_values(by='Exec. Times', ascending=True)
    print(table)
    print(table.max())