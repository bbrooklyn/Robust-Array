# Custom array class
class Array:
    def __init__(self,length,array = []):        
        if all(isinstance(x, type(array[0])) for x in array):
            if len(array) <= length:
                self.__array = array
                self.__length = length
            else:
                raise OverflowError('Actual length exceeded permitted length')
        else:
            raise TypeError('Only objects of same type are permitted')
        
    def append(self,value):
        if len(self.__array) + 1 <= self.__length:
            if len(self.__array) == 0:
                self.__array.append(value)
            else:
                if isinstance(value, type(self.__array[0])):
                    self.__array.append(value)
                else:
                    raise TypeError('Only objects of same type are permitted')
        else:
            raise OverflowError('Actual length exceeded permitted length')

    def __setitem__(self, key, value):
        if isinstance(value, type(self.__array[key])):
            self.__array[key] = value
        else:
            raise TypeError('Only objects of same type are permitted')

    def __getitem__(self, key):
        return self.__array[key]
    
    def __str__(self):
        return str(self.__array)
