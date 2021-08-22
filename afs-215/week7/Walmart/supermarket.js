class Checkout {
    constructor(){
        this.listItems = []
    }

    addItem(name, price, discount){
        var obj = {
            name:name, price:price, discount:discount
        }
        this.listItems.push(obj)
    }

    calculator(){
        var total = 0
        // console.log('calculate')
        for (var i = 0; i < this.listItems.length; i ++){
            if (!this.listItems[i].price){
                return "one of the items doesn't have a price"
            }   else{
                total += (this.listItems[i].price)
                if (this.listItems[i].discount){
                    total += (this.listItems[i].price * this.listItems[i].discount)
                }
            }

            // console.log(total)
        }
        return total
    }


}
module.exports = {Checkout}