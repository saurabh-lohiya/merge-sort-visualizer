from collections import defaultdict
from collections import deque

def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    arr1 = mergeSort(array[:mid])
    arr2 = mergeSort(array[mid:])
    return merge(arr1, arr2)


def merge(a, b):
    i = j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


origArray = [4, 2, 11, 9, 3, 1, 7]


class TreeNode:
    def __init__(self, array, left=None, right=None):
        self.val = array
        self.left = left
        self.right = right
        self.sorted = False


def traversal(root):
    if len(root.val) > 1:
        mid = len(root.val)//2
        root.left = TreeNode(root.val[:mid])
        root.right = TreeNode(root.val[mid:])
        traversal(root.left)
        traversal(root.right)
    return root


# root = TreeNode(origArray)
root = traversal(TreeNode(origArray))

def levelOrderTraversal(root):
    ans = []

    if root is None:
        return ans
    queue = deque([root])

    while queue:
        currSize, currList = len(queue), []
        for i in range(currSize):
            currNode = queue.popleft()
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
            currList.append(currNode.val)
        ans.append(currList)
    return ans

tr = levelOrderTraversal(root)
# print(tr)
for ls in tr:
    for l in ls:
        print(l, end=" ")
    print()

final = []


def mergeTree(root, final):
    # print(root.val)
    if len(root.val) == 1:
        root.sorted = True
    if root.left and root.right:
        mergeTree(root.left, final)
        mergeTree(root.right, final)
        if root.left.sorted and root.right.sorted:
            root.val = merge(root.left.val, root.right.val)
            root.sorted = True
            final.append(root.val)
    return final

def processFinalArray(final):
    final_dict = defaultdict(list)
    for arr in final:
        final_dict[len(arr)].append(arr)
    f1 = list(final_dict.values())
    return f1


f1 = processFinalArray(final)

for ls in f1:
    for l in ls:
        print(l, end=" ")
    print()
