class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.num = 0
        self.end = len(list_of_list)
    def __iter__(self):
        print("Цикл начинается")
        self.counter = 0            
        return self
    
    def __next__(self):
        if self.counter == len(self.list_of_list):
            print("Цикл завершается")      
            raise StopIteration   
        if self.num < len(self.list_of_list[self.counter])-1:   
            elem = self.list_of_list[self.counter][self.num]
            self.num+=1
            return elem
        elif self.num == len(self.list_of_list[self.counter])-1:
            elem = self.list_of_list[self.counter][self.num]     
            self.num=0       
            self.counter+=1
            return elem
        
                 
        

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
   

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]