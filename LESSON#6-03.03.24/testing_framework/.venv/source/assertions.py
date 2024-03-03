import exceptions
class Assertions:

    def __init__(self,value):
        self.value=value
        pass

    def equals_assert(self,a):
        if a!=self.value:
            raise exceptions.CustomExceptions.call("Error!, values not equal")
        return self

    def bigger_assert(self,a):
        if a<self.value:
            raise exceptions.CustomExceptions.call("Error!, values not bigger")
        return self
    
    def smaller_assert(self,a):
        if a>self.value:
            raise exceptions.CustomExceptions.call("Error!, values not smaller")
        return self
    
    def contains_assert(self,a):
        if a not in self.value:
            raise exceptions.CustomExceptions.call("Error!, values not contains")
        return self
    
    def starts_with_assert(self,a):
        
        if type(self.value)==int:
            self.value=str(self.value)
        if type(self.value)==str:
            if not self.value.startswith(a):
                raise exceptions.CustomExceptions.call("Error!, values not starts with")
            return self
        raise exceptions.CustomExceptions.call("Error!, values not starts with")

    def ends_with_assert(self,a):
        if type(self.value)==int:
            self.value=str(self.value)
        if type(self.value)==str:
            if not self.value.endswith(a):
                raise exceptions.CustomExceptions.call("Error!, values not ends with")
            return self
        raise exceptions.CustomExceptions.call("Error!, values not ends with")