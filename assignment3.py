class Location:
#initializes location of the place of living
    def __init__(self, longitude , latitude):
        self.longitude = longitude
        self.latitude = latitude

#parent
class Residence:
    priceCategorizing=['Cheap','Average Price','Expensive']

    def __init__(self,price,size,roomsCount,balkonsCount,longitude,latitude): 
        self.__price = price
        self.__size = size
        self.__roomsCount=roomsCount
        self.__balkonsCount=balkonsCount
        self.__loc = Location(longitude=longitude , latitude=latitude)

# setters ang getters

    def setPrice(self,price):
        self.__price=price

    def getPrice(self):
        return self.__price

    def setSize(self,size):
        self.__size=size
        
    def getSize(self):
        return self.__size
    
    def setRommsCount(self,count):
        self.__roomsCount=count
        
    def getRoomsCount(self):
        return self.__roomsCount

    def setBalkonsCount(self,count):
        self.__balkonsCount=count
        
    def getBalkonsCount(self):
        return self.__balkonsCount
  
    def setLocation(self,longitude , latitude):
        self.__loc=Location(longitude=longitude,latitude=latitude)
    
    def getLocation(self):
        return[self.__loc.longitude,self.__loc.latitude]
    
    def setApartmentAge(self,age):
        self.__apartmentAge=age
        
    def getApartmentPerAge(self):
        return self.__apartmentAge

    # get info
    def info(self):
        print('Price is',self.getPrice())
        if(self.getRoomsCount
        ()==1):
            print('Residence has '+str(self.getRoomsCount()) + ' room')
        else:
            print('Residence has '+str(self.getRoomsCount()) + ' rooms')
        if(self.getBalkonsCount()==1):
            print('Residence has '+str(self.getBalkonsCount()) + ' balkon')
        else:
            print('Residence has '+str(self.getBalkonsCount()) + ' balkons')

        print('Location:','(longitude: '+ str(self.__loc.longitude) + ' latitude:',str(self.__loc.latitude) + ')')
        print('Size is '+str(self.getSize())+'m')

    # categorize residences based on price
    def categorizingReseidencePrices(self):
        if(self.getPrice()< 40000):
            print('This residence is',self.priceCategorizing[0])
        elif(self.getPrice() >= 40000 and self.getPrice()< 70000):
            print('This residence is',self.priceCategorizing[1])
        elif(self.getPrice() >= 70000):
            print('This residence is',self.priceCategorizing[2]) 
    
    # change the price
    def changePrice(self,newPrice):
        self.setPrice(newPrice)
    
    # change the size of residence and change the price if needed
    def changeSize(self,size,changePrice,pricePerMeter):
        oldSize=self.getSize()
        self.setSize(size)
        newSize=self.getSize()
        oldPrice=self.getPrice()
        difference=newSize-oldSize
        if(difference>0 and changePrice==True):
            newPrice=difference*pricePerMeter
            total=oldPrice + newPrice
            self.changePrice(total)
        elif(difference<0 and changePrice==True):
            newPrice=(difference*pricePerMeter) * -1
            total = oldPrice - newPrice
            self.changePrice(total)
        



res1=Residence(0,0,0,0,0,0)
res1.setPrice(55000)
res1.setSize(150)
res1.setRommsCount(5)
res1.setBalkonsCount(1)
res1.setLocation(longitude=1111,latitude=2222)
res1.categorizingReseidencePrices()
#res1.changeSize(140,False,0)
res1.changeSize(140,True,0)
#res1.changeSize(160,True,0)
res1.info()

