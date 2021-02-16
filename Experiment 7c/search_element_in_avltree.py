class TreeNode(object): 
    def __init__(self,_val): 
        self.val = _val 
        self.left = None
        self.right = None
        self.height = 1
        
class AVL_Tree(object): 
    
    def insert(self, root, val): 
               
      
        if not root: 
            return TreeNode(val) 
        elif val < root.val: 
            root.left = self.insert(root.left, val) 
        else: 
            root.right = self.insert(root.right, val)
       
            
        root.height = 1 + max(self.Height(root.left), self.Height(root.right)) 
       
        balance = self.check_Avl(root) 
        
        
        #RR Rotation 
        if balance > 1 and val < root.left.val: 
            return self.RR(root) 

        #LL Rotation 
        if balance < -1 and val > root.right.val: 
            return self.LL(root) 
        #RL Rotation 
        if balance > 1 and val > root.left.val: 
            root.left = self.LL(root.left) 
            return self.RR(root) 
        #LR Rotation 
        if balance < -1 and val < root.right.val: 
            root.right = self.RR(root.right) 
            return self.LL(root) 
  
        return root 
     #LL Rotation
    def LL(self, node): 
       
        p = node.right 
      
        p.left = node 
        node.right = t 
        
        node.height = 1 + max(self.Height(node.left), self.Height(node.right)) 
        p.height = 1 + max(self.Height(p.left), self.Height(p.right)) 
   
        return p 
    #LL Rotation
    def RR(self, node): 
  
        p = node.left 
        t = p.right
     
        p.right = node
        node.left = t 
       
        node.height = 1 + max(self.Height(node.left), self.Height(node.right)) 
        p.height = 1 + max(self.Height(p.left), self.Height(p.right)) 
        return p 
   
    def Height(self, root): 
        if not root: 
            return 0
  
        return root.height 
    
    def check_Avl(self, root): 
        if not root: 
            return 0
  
        return self.Height(root.left) - self.Height(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 


def insert_data(_data):
        mytree = AVL_Tree()
        root = None
        for i in _data:
            root = mytree.insert(root,i)
        print("Preorder Traversal of constructed AVL tree is:")
        mytree.preOrder(root)
        print()
        return root
def Search(root,val):
    if (root is None):
        return False
    elif (root.val == val):
        return True
    elif(root.val < val):
        return Search(root.right,val)
    return Search(root.left,val)
    return False

def main():
    root = insert_data([10,8,15,7,9,12,17,16,18,6,4])
    t = int(input('Enter the key to be searched:\t'))
    if(Search(root,t)):
        print()
        print('"Element found in AVL Tree"')
    else:
        print()
        print('"Element not found in AVL Tree"')
if __name__ == "__main__":
    main()
else:
    pass
