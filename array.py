import ctypes

class Array:
    def __init__(self):
        self.len=0
        self.space=1

        self._array= self._create_array(self.space)


    def _create_array(self,size):
        return (ctypes.py_object*size)()


    def __getitem__(self, index):
        if not 0<=index<self.len: raise IndexError("Invalid index or index out of range")
        return self._array[index]


    def insert(self,item, index):
        if self.len==self.space:
            self._extend_array(2*self.space)
        if not 0<=index<self.len: raise IndexError("Invalid index or index out of range")
        for i in range(self.len, index, -1):
            self._array[i]=self._array[i-1]
        self._array[index]=item
        self.len +=1


    def _extend_array(self, range):
        new_array = self._create_array(range)
        for i in range(self.len):
            new_array[i]= self._array[i]
        self._array=new_array
        self._space=range

    def __delete__(self, index=-1):

        for i in range(index,self.len):
            self._array[i]=self._array[i+1]
        self.len -=1






