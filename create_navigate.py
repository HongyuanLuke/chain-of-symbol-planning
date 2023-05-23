import random
import json
class TreeNode:
    def __init__(self, val, label, distance):
        self.val = val
        self.label = label
        self.distance = distance
        self.parent_label = None
        self.left = None
        self.right = None
        self.type = None
        if label:
            self.type = label.split()[0]

def insert(root, val, label, distance, parent_label=None):
    if not root:
        node = TreeNode(val, label, distance)
        node.parent_label = parent_label
        return node
    if val < root.val:
        root.left = insert(root.left, val, label, distance, root.label)
    else:
        root.right = insert(root.right, val, label, distance, root.label)
    return root

def inorder_traversal(root, desc_list):
    if not root:
        return
    #print(root.val, root.label, root.parent_label)
    if root.parent_label:
        desc_cur = 'There is a road which is ' + str(root.distance) + ' meters long from '+ root.parent_label + ' to ' + root.label + '. '
        desc_list.append(desc_cur)
    inorder_traversal(root.left, desc_list)
    inorder_traversal(root.right, desc_list)
    
def find_all_node(root, label, node_list):
    if not root:
        return None
    if root.type == label:
        node_list.append(root)
    #if label < root.val:
    find_all_node(root.left, label, node_list)
    find_all_node(root.right, label, node_list)
def find_node(root, val, path, distance):
    if root:
        path.append(root.label)
    if root:
        distance += root.distance
    if not root:
        return distance
    if root.val == val:
        return distance
    if val < root.val:
        distance = find_node(root.left, val, path, distance)
    else:
        distance = find_node(root.right, val, path, distance)
    return distance
def find_distance(root, node):
    #node = find_node(root, label)
    if not node:
        return None
    path = []
    #path.append(node.label)
    distance_sum = 0
    distance_sum =find_node(root, node.val, path, distance_sum)
    
    return distance_sum, path

def get_all_type(root, type_list):
    #node = find_node(root, label)
    if not root:
        return None
    
    type_list.append(root.type)
    #if label < root.val:
    get_all_type(root.left, type_list)
    get_all_type(root.right, type_list)

def find_min_index(lst):
    if not lst:
        return None
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    return min_index
flag = 65
n = 10
root = None
labels = ["store", "bank", "house", "cinema", "garden", "school"]
res_all = []
for step in range(500):
    root = None
    print(step)
    label_list = [chr(i+flag) for i in range(10)]
    distances = [100, 200]
    n = random.randint(7, 10)
    print(n)
    for i in range(n):
      val = random.randint(1, 100)
      #label = "Node " + str(i+1)
      label = random.choice(labels)
      label_res = random.choice(label_list)
      label_list.remove(label_res)
      label = label +' ' + label_res
      if i == 0:
          distance = 0
      else:
          distance = random.choice(distances)
      root = insert(root, val, label, distance)
    descp = 'There is a set of roads and a set of landmarks. The start point is {}. '.format(root.label)
    label_cur = labels
    type_list = []
    get_all_type(root, type_list)
    #print('type_list', list(set(type_list[1:])))
    type_list = list(set(type_list[1:]))
    #print('label_cur', label_cur)
    for item in type_list:
        if item in root.label.split():
            #print(1, item)
            type_list.remove(item)
    label_ = random.choice(type_list)
    q = 'From the start point, how to reach the nearest {}?'.format(label_)
    node_list = []
    find_all_node(root, label_, node_list)
    
    answer_all = []
    list_all = []
    for item in node_list:
        distance_sum, path = find_distance(root, item)
        #print(distance_sum)
        answer = (distance_sum, path)
        list_all.append(distance_sum)
        answer_all.append(path)
    #print(len(answer_all))
    min_index = find_min_index(list_all)
    #print('all:', answer_all)
    #print(answer_all[min_index])
    answer_final = ''
    for item in answer_all[min_index]:
        item_new = item.split()[1]
        answer_final+= item_new
    #print(answer_final)
    
    '''
    for item in answer_all:
        (distance_sum, path) = item
        print(path)
        print('question', q)
    '''
    #print('question', q)
    descp_list = []
    
    lst = [5, 3, 8, 2, 9, 1]
    #min_index = find_min_index(lst)
    inorder_traversal(root, descp_list)
    #print(descp_list)
    for item in descp_list:
      descp += item
    print(len(descp_list))
    #print(descp_list)
    res = {'Story': descp, 'Question': q, 'Answer': answer_final}
    res_all.append(res)
    #print(descp)
with open('../data/navigation_data/navigation_data.json', 'w') as outfile:
        json.dump(res_all, outfile)



