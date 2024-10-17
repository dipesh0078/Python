#28.How do you implement custom set-like behavior in a class?


class CustomSet:
    def __init__(self, elements=None):
        self.elements=[]
        if elements is not None:
            for element in elements:
                self.add(element)
    
    def __contains__(self,item):
    #check if an item is in the set.
         return item in self.elements
    
    def __len__(self):
        return len(self.elements)
    
    def __iter__(self):
        return iter(self.elements)
    
    def add(self,item):
        if item not in self.elements:
           self.elements.append(item)
    
    def remove(self,item):
        if item in self.elements:
            self.elements.remove(item)
        else:
            raise KeyError('Item not found')
    

    def __repr__(self):
        """Return a string representation of the set."""
        return f"CustomSet({self.elements})"

my_set = CustomSet([1, 2, 3])
my_set.add(4)
print(my_set)  
print(2 in my_set)  
print(len(my_set)) 
my_set.remove(2)
print(my_set) 