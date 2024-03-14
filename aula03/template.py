class Node:
    def __init__(self, v, w=0):
        self.v = v
        self.w = w
        self.adj = []
    
    def link(self, n):
        self.adj.append(n)

  
class Graph:
    def __init__(self, size):
        self.size = size
        self.vertex = [Node(i) for i in range(size)]

    def __getitem__(self, i):
        return self.vertex[i]
    
    def link(self, n1, n2):
        self.vertex[n1].link(n2)
    

class UnionFind:
    def __init__(self, n):
        self.set_size = [1 for _ in range(n)]
        self.rank = [0 for _ in range(n)]
        self.p = [i for i in range(n)]
        self.num_sets = n

    def find_set(self, i):
        if self.p[i] == i:
            return i

        self.p[i] = self.find_set(self.p[i])
        return self.p[i]
    
    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)
    
    def union_set(self, i, j):
        if self.is_same_set(i, j):
            return 
        
        self.num_sets -= 1
        x, y = self.find_set(i), self.find_set(j)

        if self.rank[x] > self.rank[y]:
            self.p[y] = x
            self.set_size[x] += self.set_size[y]
        else:
            self.p[x] = y
            self.set_size[y] += self.set_size[x]

            self.rank[y] += 1 if self.rank[x] == self.rank[y] else 0
    
    def num_disjoint_sets(self):
        return self.num_sets
    
    def size_of_set(self, i):
        return self.set_size[self.find_set(i)]


def main():
    print("Assume that there are 5 disjoint sets initially")

    uf = UnionFind(5)

    print(f"{uf.num_disjoint_sets()}")
    uf.union_set(0, 1)
    print(f"{uf.num_disjoint_sets()}")
    uf.union_set(2, 3)
    print(f"{uf.num_disjoint_sets()}")
    uf.union_set(4, 3)
    print(f"{uf.num_disjoint_sets()}")

    print(f"is_same_set(0, 3) = {uf.is_same_set(0, 3)}")
    print(f"is_same_set(0, 3) = {uf.is_same_set(4, 3)}")

    for i in range(5):
        print(f"find_set({i}) = {uf.find_set(i)} - size_of_set({i}) = {uf.size_of_set(i)}")

    uf.union_set(0, 3)
    print(f"{uf.num_disjoint_sets()}")

    for i in range(5):
        print(f"find_set({i}) = {uf.find_set(i)} - size_of_set({i}) = {uf.size_of_set(i)}")



if __name__ == "__main__":
    main()