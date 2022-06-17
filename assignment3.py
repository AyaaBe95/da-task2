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
        



#res1=Residence(0,0,0,0,0,0)
#res1.setPrice(55000)
#res1.setSize(150)
#res1.setRommsCount(5)
#res1.setBalkonsCount(1)
#res1.setLocation(longitude=1111,latitude=2222)
#res1.categorizingReseidencePrices()
#res1.changeSize(140,False,0)
#res1.changeSize(140,True,0)
#res1.changeSize(160,True,0)
#res1.info()

# ----------------------------------------------------------------

class Villa(Residence):
    def __init__(self,__price,__size,__roomsCount,__balkonCount,__longitude,__latitude):
        super().__init__(__price,__size,__roomsCount,__balkonCount,__longitude,__latitude)
        self.__floorsCount=0
        self.__gardenHeight=0
        self.__gardenWidth=0
        self.__changes=''

    # seters and getters
    def setFloorsCount(self,count):
        self.__floorsCount=count
        
    def getFloorsCount(self):
        return self.__floorsCount

    def setGardenHeight(self,height):
        self.__gardenHeight=height
        
    def getGardenHeight(self):
        return self.__gardenHeight

    def setGardenWidth(self,width):
        self.__gardenWidth=width
        
    def getGardenWidth(self):
        return self.__gardenWidth
    
    def setChanges(self,changes):
        self.__changes=changes
    
    def getChanges(self):
        return self.__changes
    
    def splitChanges(self):
        lowerStr= self.getChanges().lower()
        splitedStr = lowerStr.split(',')
        return splitedStr


    # calculate the area of garden
    def getGardenArea(self):
        height= self.getGardenHeight()
        width=self.getGardenWidth()
        area=0
        if(height==width):
            area=height*width
        else:
            area=2*(height+width)
        return area

    def info(self):
        print('Villa has '+str(self.getFloorsCount()) + ' floor')
        print('Garden area is '+str(self.getGardenArea()) + 'mm')
        print('This villa needs some changes:' , self.splitChanges())
        return super().info()
    

villa1=Villa(25000,150,4,2,111,222)
villa2=Villa(25000,150,4,2,111,222)

villa1.setRommsCount(3)
villa1.setFloorsCount(2)
villa1.setBalkonsCount(2)
villa1.setGardenHeight(20)
villa1.setGardenWidth(10)
villa1.changePrice(66000)
villa1.setChanges('paint,tree planting')

villa1.info()


