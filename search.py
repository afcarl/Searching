import collections

class Bfs:

    def __init__(self, start, stop, tree):
        '''start := str  start element
           stop  := str  stop element
           tree  := dict format:
                    {From : [ToA, ToB, ..., To?],
                    From is the parent node of the To? nodes.
                    The node ToA would have the line as follows, for example,
                    ToA  : [From, To1, To2, ..., To?], ... }'''

        self.start = start
        self.stop  = stop
        self.tree  = tree
        self.queue = collections.deque([[self.start]])
        self.valid = collections.deque()

    def step(self):
        '''One step of the searching algorithm, called from search'''
        current = self.queue.popleft()
        parent  = current[-1]
        nodes   = self.tree[parent]

        for node in nodes:
            if node not in current:
                self.queue.append(current + [node])
            else:
                continue
            if self.stop == node:
                return True
        return False

    def search(self):
        '''Search from start to stop'''
        while self.queue:
            if self.step():
                self.valid.append(self.queue.pop())
        return self.valid
