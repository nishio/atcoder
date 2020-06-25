

import sys


def main():
    def _siftdown(heap, startpos, pos):
        newitem = heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if newitem < parent:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem

    def _siftup(heap, pos):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        heap[pos] = newitem
        _siftdown(heap, startpos, pos)

    def heappush(heap, item):
        """Push item onto heap, maintaining the heap invariant."""
        heap.append(item)
        _siftdown(heap, 0, len(heap)-1)

    def heappop(heap):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            _siftup(heap, 0)
            return returnitem
        return lastelt

    def heapreplace(heap, item):
        """Pop and return the current smallest value, and add the new item.
        This is more efficient than heappop() followed by heappush(), and can be
        more appropriate when using a fixed-size heap.  Note that the value
        returned may be larger than item!  That constrains reasonable uses of
        this routine unless written as part of a conditional replacement:
            if item > heap[0]:
                item = heapreplace(heap, item)
        """
        returnitem = heap[0]    # raises appropriate IndexError if heap is empty
        heap[0] = item
        _siftup(heap, 0)
        return returnitem

    def heappushpop(heap, item):
        """Fast version of a heappush followed by a heappop."""
        if heap and heap[0] < item:
            item, heap[0] = heap[0], item
            _siftup(heap, 0)
        return item

    def heapify(x):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        n = len(x)
        # Transform bottom-up.  The largest index there's any point to looking at
        # is the largest with a child index in-range, so must have 2*i + 1 < n,
        # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
        # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
        # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
        for i in reversed(range(n//2)):
            _siftup(x, i)

    def _heappop_max(heap):
        """Maxheap version of a heappop."""
        lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            _siftup_max(heap, 0)
            return returnitem
        return lastelt

    def _heapreplace_max(heap, item):
        """Maxheap version of a heappop followed by a heappush."""
        returnitem = heap[0]    # raises appropriate IndexError if heap is empty
        heap[0] = item
        _siftup_max(heap, 0)
        return returnitem

    def _heapify_max(x):
        """Transform list into a maxheap, in-place, in O(len(x)) time."""
        n = len(x)
        for i in reversed(range(n//2)):
            _siftup_max(x, i)


def _test():
    import doctest
    doctest.testmod()


USE_NUMBA = False
if USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE' or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'void()')(main)
    # b1: bool, i4: int32, i8: int64, double: f8, [:], [:, :]
    cc.compile()
    exit()
else:
    if USE_NUMBA and sys.argv[-1] != '-p':
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import main  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        exit()
    elif len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline

    # read parameter
    main()
