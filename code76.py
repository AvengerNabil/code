import sys
sys.setrecursionlimit(1 << 25)

def input():
    return sys.stdin.readline().strip()

# DSU for removed cells (4-adjacency), with tracking whether a component touches outside
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1]*n
        self.out = [False]*n  # whether component connects to outside
    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a
    def union(self, a, b):
        a = self.find(a); b = self.find(b)
        if a == b: return a
        if self.sz[a] < self.sz[b]: a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]
        self.out[a] = self.out[a] or self.out[b]
        return a

def main():
    n_line = input()
    if not n_line:
        return
    n = int(n_line)
    t = int(input())
    coords = []
    for i in range(n):
        r,c = map(int, input().split())
        coords.append((r,c))
    # map coordinates to index (0-based)
    pos2id = {coords[i]: i for i in range(n)}

    # precompute 8-neighbors (indices) and 4-neighbors coordinates
    neigh8 = [[] for _ in range(n)]
    neigh4coords = [[] for _ in range(n)]
    for i,(r,c) in enumerate(coords):
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr==0 and dc==0: continue
                rr, cc = r+dr, c+dc
                if (rr,cc) in pos2id:
                    neigh8[i].append(pos2id[(rr,cc)])
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            neigh4coords[i].append((r+dr,c+dc))

    # removed flag (True if removed -> empty in reverse process)
    removed = [False]*n

    # DSU over removed cells; we will lazily give ids to removed cells:
    # map removed index -> its DSU index (0..k-1) as they are removed
    removed_id = [-1]*n
    dsu = DSU(n)  # we can allocate n slots; only use for removed cells
    # Note: we will use element i in DSU when cell i has been removed -> removed_id[i] = i

    # helper: whether removed-component of cell i connects to outside
    # We detect outside connection at time of removal: if any 4-neighbor coordinate is not in pos2id,
    # then that removed cell's DSU component is connected to outside.
    # Also union with any already-removed 4-neighbors.

    # helper: check if cell i is 4-reachable from outside now:
    def is_4_reachable(i):
        # a cell i (occupied) is 4-reachable if it has a 4-neighbor that is removed and whose component is connected to outside,
        # or if a 4-neighbor coordinate is not in the city at all (then that neighbor is empty external cell)
        for (nr,nc) in neigh4coords[i]:
            if (nr,nc) not in pos2id:
                # neighbor is an empty cell leading immediately to outside
                return True
            j = pos2id[(nr,nc)]
            if removed[j]:
                # removed j exists in DSU and maybe connected to outside
                root = dsu.find(j)
                if dsu.out[root]:
                    return True
        return False

    # For DSU usage: we only use node id equal to original index for removed nodes.
    # When we remove i, we set removed[i]=True, removed_id[i]=i, and union with removed 4-neighbors.
    def remove_cell(i):
        removed[i] = True
        # in this implementation we use DSU index = i
        # set 'out' flag if any 4-neighbor coordinate is not in pos2id
        root = dsu.find(i)
        out_flag = False
        for (nr,nc) in neigh4coords[i]:
            if (nr,nc) not in pos2id:
                out_flag = True
                break
        dsu.out[root] = dsu.out[root] or out_flag
        # union with removed 4-neighbors
        for (nr,nc) in neigh4coords[i]:
            if (nr,nc) in pos2id:
                j = pos2id[(nr,nc)]
                if removed[j]:
                    dsu.union(i, j)

    # Check whether vertex v is an articulation point in current 8-graph of occupied vertices.
    # We must consider only not-removed vertices; we test if removing v disconnects its 8-neighbors.
    def is_8_articulation(v):
        # collect occupied 8-neighbors
        neigh = [u for u in neigh8[v] if not removed[u]]
        if len(neigh) <= 1:
            return False  # cannot split if 0 or 1 neighbor
        # pick start = neigh[0], DFS among occupied nodes skipping v
        start = neigh[0]
        stack = [start]
        seen = set([start])
        while stack:
            cur = stack.pop()
            for w in neigh8[cur]:
                if w == v or removed[w]: continue
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        # if all neighbors are in seen -> not an articulation
        for u in neigh:
            if u not in seen:
                return True
        return False

    # Precompute initial candidates: occupied cells that are 4-reachable and not 8-articulation
    import heapq
    # For t=2 we need to pick largest index among candidates -> use max-heap by pushing -index
    # For t=1 we may pick arbitrary -> we'll still pick by index ascending for simplicity
    # We'll maintain a heap of candidate indices (for t=2 use negative to make it max).
    heap = []
    in_heap = [False]*n

    def push_if_candidate(i):
        if removed[i]:
            return
        if is_4_reachable(i) and not is_8_articulation(i):
            if not in_heap[i]:
                if t == 2:
                    heapq.heappush(heap, (- (i+1), i))  # store i with key -index for max behavior (1-based tie)
                else:
                    heapq.heappush(heap, (i+1, i))
                in_heap[i] = True

    # Initially, before any removals, only vertices that are 4-reachable are those that have a 4-neighbor not in pos2id.
    # Push all that are currently candidate.
    for i in range(n):
        # quick check: does vertex have any 4-neighbor coordinate outside the city?
        has_outside_adj = False
        for (nr,nc) in neigh4coords[i]:
            if (nr,nc) not in pos2id:
                has_outside_adj = True
                break
        if has_outside_adj:
            # verify not articulation
            if not is_8_articulation(i):
                if t == 2:
                    heapq.heappush(heap, (-(i+1), i))
                else:
                    heapq.heappush(heap, (i+1, i))
                in_heap[i] = True

    removal_order = []
    # Repeatedly remove n vertices
    while heap and len(removal_order) < n:
        _, v = heapq.heappop(heap)
        in_heap[v] = False
        # candidate might have become invalid since push; re-check
        if removed[v]:
            continue
        if not is_4_reachable(v):
            continue
        if is_8_articulation(v):
            continue
        # remove it
        remove_cell(v)
        removal_order.append(v)
        # neighbors (8 and 4) may become new candidates; push them
        for u in neigh8[v]:
            if not removed[u]:
                push_if_candidate(u)
        # also 4-neighbors who were occupied might become reachable
        for (nr,nc) in neigh4coords[v]:
            if (nr,nc) in pos2id:
                u = pos2id[(nr,nc)]
                if not removed[u]:
                    push_if_candidate(u)

    if len(removal_order) != n:
        print("NO")
        return

    # removal_order is sequence of indices removed in reverse building order: sn, sn-1, ..., s1
    # we need to output s1..sn (build order) so reverse the list and convert to 1-based indices
    build_order = list(reversed(removal_order))
    print("YES")
    for idx in build_order:
        print(idx+1)

if __name__ == "__main__":
    main()
#https://codeforces.com/problemset/problem/1192/A