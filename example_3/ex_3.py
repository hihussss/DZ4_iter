class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.num = 0
        self.numeric = 0
        self.end = len(list_of_list)
    def __iter__(self):
        print("Цикл начинается")
        self.counter = 0            
        return self
    
    def __next__(self):
        if self.counter == len(self.list_of_list) or self.num == 4:
            print("Цикл завершается")      
            raise StopIteration
        elif self.num < len(self.list_of_list[self.counter])-1:  
            elem = self.list_of_list[self.counter][self.num]
            
            if isinstance(elem, list):
                elem = elem[self.numeric]
                if len(self.list_of_list[self.counter][self.num])>1:
                    self.numeric+=1
                    
                if self.numeric==len(self.list_of_list[self.counter][self.num]):
                    self.numeric=0
                    
            if isinstance(elem, list):
                elem = "".join(str(elem)).replace("[", "").replace("]", "").replace("'", "").replace("\n", "").replace(" ", "")        
                
            if elem=="!":
                self.num+=1
            else:
                self.num+=1                
            print(type(elem))  
            return elem
        elif self.num == len(self.list_of_list[self.counter])-1:
            elem = self.list_of_list[self.counter][self.num]
                  
             
            if isinstance(elem, list):
                elem = elem[self.numeric]
                if len(self.list_of_list[self.counter][self.num])>1:
                    self.numeric+=1
                if self.numeric==len(self.list_of_list[self.counter][self.num]):
                    self.num=0
                    self.counter+=1
                    self.numeric=0           
            if isinstance(elem, list):
                elem = "".join(elem).replace("[", "").replace("]", "").replace("'", "").replace("\n", "").replace(" ", "")    
            if isinstance(elem, str):    
                elem = elem.replace("[", "").replace("]", "").replace("'", "").replace("\n", "").replace(" ", "")   
            else:
                self.counter+=1
                self.num=0  
            print(type(elem))               
            return elem       

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']