"""
SUCCESSOR DATA STRUCTURE
* Sang Doan. Nov 7, 2022.
* Data structure that can remove and find immediate successors of a subsequence of 1,...,n in logarithmic time.
    Given a set of n integers S = {0, 1,..., n − 1}. This data structure can perform the following operations:
        - Remove x from S (Θ(1) time complexity)
        - Find the successor of x — the smallest y in S such that y ≥ x (Θ(lg n) time complexity).
"""

class SuccessorWithDelete:

    def __init__(self, n:int) -> None:
        if n <= 0:
            raise ValueError("The size of the union must be greater than 1")
        self.n = n
        self._successor = list(range(self.n))
        self._size = [1] * self.n

    def check_valid(self, a:int) -> None:
        if a < 0 or a > self.n - 1:
            raise ValueError(f"{a} is not a valid element id")
        return
    
    def successor(self, a:int) -> int:
        """Finding successor of a with path compression
        """
        self.check_valid(a)

        while a != self._successor[a]:
            prev = a
            a = self._successor[a]
            self._successor[prev] = a
        return a

    def remove(self, a:int) -> None:
        """Remove a, i.e. set successor of a to be the successor of the successor of a
        """
        self.check_valid(a)
        self._successor[a] = self.successor(a + 1)
        return


# Dynamic Connectivity Client
def main():
    n = int(input())
    SD = SuccessorWithDelete(n)

    try:
        while True:
            cmd, a = input().split()
            match cmd:
                case "rm":
                    SD.remove(int(a))
                    print(f"Removed {a}.")
                case "suc":
                    print(f"The successor of {a} is: {SD.successor(int(a))}.")
                case _:
                    print(f"Invalid command.")
    except ValueError:
        print("End of input")

    return


if __name__ == "__main__":
    main()