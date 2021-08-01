class Checkout () :                     
    listItems = []
    print(listItems)

    def __init__(self):
        return None
    def addItem(self, item):
        self.listItems.append(item)
    def addPrice(self, name, price):
        if name in self.listItems:
            index = self.listItems.index(name)
            print(index)
            self.listItems[index].append(price)
        else :
            name.append(price) 
            self.listItems.append(name)
    def calculator(self): 
        totalCount = 0

        for item in self.listItems:
            if len(item) >= 2:
                num = item [1]
                if len(item) == 3:
                    num = item[1] * item[2]
                totalCount += num  
            else:
                print("Item " + item[0] + " does not have a price and is not added to total")
                

               
                
        self.currentValue = totalCount
    def addDiscount(self, item, price, discount):
        if item in self.listItems:
            index = self.listItems.index(item)
            print(index)
            self.listItems[index].append(discount)
        else :
            item.append(price)
            item.append(discount) 
            self.listItems.append(item)

                 

