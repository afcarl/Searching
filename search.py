import collections

class Bfs:

    def __init__(self, start, stop, tree, debug=False):
        '''start := str  start element
           stop  := str  stop element
           tree  := dict format:
                    {From : [ToA, ToB, ..., To?],
                    From is the parent node of the To? nodes.
                    The node ToA would have the line as follows, for example,
                    ToA  : [From, To1, To2, ..., To?], ... }
           debug := bool give print out of process default False'''

        self.start = start
        self.stop  = stop
        self.tree  = tree
        self.queue = collections.deque([[self.start]])
        self.valid = collections.deque()
        self.debug = debug

    def step(self):
        '''One step of the searching algorithm, called from search'''
        current = self.queue.popleft()
        parent  = current[-1]
        nodes   = self.tree[parent]

        for node in nodes:
            if self.debug: self.printer(1, current, node)                       # debug line
            if node not in current:
                self.queue.append(current + [node])
                if self.debug: self.printer(2)                                  # debug line
            else:
                if self.debug: self.printer(3, None, node)                      # debug line
                continue
            if self.stop == node:
                if self.debug: self.printer(4)                                  # debug line
                return True
        return False

    def search(self):
        '''Search from start to stop'''
        while self.queue:
            if self.step():
                self.valid.append(self.queue.pop())
                if self.debug: self.printer(5)                                  # debug line
        return self.valid

#------------------------------------------------------------------------------  Method used only when debug is True
    def printer(self, line, current=None, node=None):
        '''Print out for debug mode'''
        if line == 1:
            print 'Current + node: ', current + [node]  # 1
        elif line == 2:
            print '+++ Queue: ', self.queue  # 2
        elif line == 3:
            print '--- Remove above because %s doubles ' % (node)
            print '-=-=-=-=-=-=-=-=-=-=-=-=-=-='
        elif line == 4:
            print '!!!' + 'Found Stop'.center(25, '~')
        elif line == 5:
            print 'Valid path: ', self.valid
#------------------------------------------------------------------------------  Method used only when debug is True
