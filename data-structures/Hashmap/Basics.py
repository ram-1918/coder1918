''' Complexities 
> Access, insert, update, delete: O(1), O(n)
> traversing, searching, resizing, coping, keylookup: O(n)
> merging: O(m)
'''

''' Dictionary Methods: no duplications, ordered, mutable, multiple datatypes, immutables as keys
dic.keys(), dic.values(), dic.items(), dic.pop(key), dic.copy(), 
dic.update(), del dic[key], dic.clear(), dic.fromkeys(), dic.get()
dic.popitem(), dic.setdefault()
'''

''' Hashmap
Limitations:
> More memory usage than other data structures, as it stores both keys and values
and also comes with an overhead of underlying hash table (empty slots, hash functions)
> Unordered: ordered from python 3.7+ or can use collections.OrderedDict()
> Hash collisions: sometimes 2 keys can have same hash value then it can be resolved through chaining
> Immutable keys like strings, integers, tuples unlike mutable ones like lists, dicts, sets 
because if their content changes their hash value changes

Trade-offs:
> Speed vs memory: speed efficient, comes with the cost of memory as it needs to store metadata like hash values, pointers
> complexity: when handling edge cases like collisions, resizing, choosing a hash function
> overhead: in case of high collision rates, it needs to rehash leading to O(n) operations

Edge-cases:
> High collision rate: if hash function is not well distributed or if a dataset has a many similar keys
> resizing overhead
> deletion and memory leaks: when an element is deleted, if not handled properly, then there can be ghost entries especially with 
custom implementations or with strict memory constaints
> iterating during modification: use copy of keys or use collections.defaultdict
> key error: use hashmap.get() or collections.defaultdict()
> when using custom objects as keys, implement __hash__, __eq__
'''


''' Set Methods: no duplicates, unordered, mutable, multiple datatypes, immutable elements only
s.add(), s.update(newSet), s.remove(), s.pop(), s.discard(), s.copy(), s.clear(), 
s.union(set2), s.intersection(set2), s.difference(set2), s.symmetric_difference()
s.intersection_update(), s.difference_update(), s.symmetric_difference_update(), 
s.issubset(), s.issuperset(), s.isdisjoint()
'''

''' Sets
Limitations:
> Unordered, mutable elements are not allowed, no duplicate elements, 
> do not support indexing, slicing, accessing elements with an index

Trade-offs:
> consumes more memory like dictionaries, as it needs to store hash values and maintain unique elements
> poorly sitributed hash function leads to collisions

Edge-cases:
> Hash collisions, keyerror on removal, copying and mutating, combining different element types
'''


