from queue import PriorityQueue

pq = PriorityQueue()
pq.put((3, 'Ann'))
pq.put((2, 'Bob'))
pq.put((4, 'Chloe'))
pq.put((1, 'Dorothy'))

print(pq.get()[1])  # Dorothy
print(pq.get()[1])  # Bob
print(pq.get()[1])  # Ann
print(pq.get()[1])  # Chloeㅅ