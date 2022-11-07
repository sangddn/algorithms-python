"""
UNION-FIND ALGORITHMS
* Sang Doan. Nov 7, 2022.
* Fun with DSU — 5 algorithms:
* (1) Quick Find (eager),
* (2) Quick Union (lazy),
* (3) Weighted Quick Union,
* (4) Quick Union with Path Compression,
* (5) Weighted Quick Union with Path Compression.
"""

class UF:
    class QuickFind:
        """Quick-Find (eager approach). 
        Time complexity (tight bound for worst case):
            - Constructor: Θ(N).
            - Union: Θ(n).
            - Check connection: Θ(1).
        """
        def __init__(self, n: int) -> None:
            self.n = n
            self.id = list(range(n))

        def union(self, p: int, q: int) -> None:
            for i in range(self.n):
                if self.id[i] == self.id[q]:
                    self.id[i] = self.id[p]

        def connected(self, p: int, q: int) -> bool:
            return self.id[p] == self.id[q]

    class QuickUnion:
        """Quick-Union (lazy approach - don't do the computation until you have to).
        Time complexity:
            - Constructor: Θ(N).
            - Union: O(n).
            - Check connection: O(n).
        """
        def __init__(self, n: int) -> None:
            self.n = n
            self.id = list(range(n))
        
        def _root(self, p: int) -> int:
            while self.id[p] != p: 
                p = self.id[p]
            return p

        def union(self, p: int, q: int) -> None:
            self.id[self._root(p)] = self._root(q)
        
        def connected(self, p: int, q: int) -> bool:
            return self._root(p) == self._root(q)
    
    class WeightedQuickUnion(QuickUnion):
        """Weighted Quick-Union
        Time complexity:
            - Constructor: Θ(N). 
            - Union: O(lg n).
            - Check connection: O(lg n).
        """
        def __init__(self, n: int) -> None:
            super().__init__(n)
            self.sz = [1] * n

        def union(self, p: int, q: int) -> None:
            p_root, q_root = self._root(p), self._root(q)
            if self.sz[p_root] > self.sz[q_root]:
                p_root, q_root = q_root, p_root

            self.id[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
    
    class QuickUnionPC(QuickUnion):
        """Quick-Union with Path Compression
        """
        def __init__(self, n: int) -> None:
            super().__init__(n)
            self.sz = list(range(n))

        def _root(self, p: int) -> int:
            while self.id[p] != p:
                temp = self.id[p]
                self.id[p] = self.id[temp]
                p = temp
            return p

        def union(self, p: int, q: int) -> None:
            """Union 2 roots by pointing the smaller to the greater
            """
            p_root, q_root = self._root(p), self._root(q)
            if p_root > q_root: p_root, q_root = q_root, p_root
            self.id[p_root] = q_root

        def find(self, p: int) -> int:
            """Find the greatest node of a connected component, which
            should be the root.
            """
            return self._root(p)
    
    class WQUPC(WeightedQuickUnion, QuickUnionPC):
        """Weighted Quick-Union with Path Compression
        Time complexity:
            - Constructor: Θ(N).
            - Union: Amortized Θ(1).
            - Check connection: Amortized Θ(1).
        """
        def __init__(self, n: int) -> None:
            super().__init__(n)


# Dynamic Connectivity Client
if __name__ == '__main__':
    n = int(input())
    uf = UF.WQUPC(n)

    try:
        while True:
            p, q = map(int, input().split())
            if not uf.connected(p, q):
                uf.union(p, q)
                print("Added Connection!")
    except ValueError:
        print("End of input")
    finally:
        print(list(range(n)))
        print(uf.id)
        print(uf.find(1))