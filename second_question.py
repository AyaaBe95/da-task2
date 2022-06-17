class Class1:

    def checkRepetionOfNumbers(self,data):
        occurences = {}
        for i in data:
            if(i in occurences):
                occurences[i] +=1
            else:
                occurences[i] =1
            list_of_tuples = list(occurences.items())
        print(list_of_tuples)



class Class2(Class1):
    def __init__(self):
        super().__init__()
        
    def checkRepetionOfNumbers(self, data):
        return super().checkRepetionOfNumbers(data) 


cls2=Class2()
data=[1,1,1,2,2,3]

cls2.checkRepetionOfNumbers(data)

     