def leftover_bidders(bids, number_of_items):
  myQueue = MySpecialQueue()

  for bid in bids:
    myQueue.insert(bid)
  for sale in range(number_of_items):
    myQueue.dequeue()
  
  return myQueue.queue if myQueue.queue else [None]

class MySpecialQueue:
  def __init__(self):
    self.queue = []

  def insert(self, data):
    self.queue.append(data)

  def dequeue(self):
    new_queue = []
    max_value = max(self.queue)
    done = False
    len_quene = len(self.queue)
    for i in range(len_quene):
      left = self.queue.pop(0)
      if left == max_value and done==False:
        done = True
      else:
        self.insert(left)


