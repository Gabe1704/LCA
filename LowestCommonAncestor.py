#LCA

# Binary Tree Node Class to help with LCA
class Node:
    def __init__(self, value):
        self.value =  value
        self.left = None
        self.right = None

# Finds route from root to x and stores in route, if route is returned return true otherwise return false
def findRoute( root, route, x):
# Check for fail
    if root == None:
        return False

    route.append(root.value)

    if root.value == x :
        return True

    # See if x is in left or right
    if ((root.left != None and findRoute(root.left, route, x)) or
            (root.right!= None and findRoute(root.right, route, x))):
        return True

    # If something is not there return false
    route.pop()
    return False

# LCA
def LCA(root, n1, n2):

    route1 = []
    route2 = []

    if (not findRoute(root, route1, n1) or not findRoute(root, route2, n2)):
        return -1

    i = 0
    while(i < len(route1) and i < len(route2)):
        if route1[i] != route2[i]:
            break
        i += 1
    return route1[i-1]
