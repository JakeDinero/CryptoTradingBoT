import cbpro
import requests as reqs

public_client = cbpro.PublicClient()

# Live updates
wsClient = cbpro.WebsocketClient(url= "wss://ws-feeed.pro.coinbase.com",products=["BTC-USD","ETH-USD"],channels= ["ticker"])


# Look up Products
print(public_client.get_products())
# r = reqs.get('https://pro.coinbase.com/products/ETH-USD')
# r2 = r.text()
# print(r2)


# Class for executing orders
class Orders: 
    def __init__(self, url, orderType, productID, stop, stop_price):
        self.url = 'https://pro.coinbase.com/orders'
        self.orderType = orderType
        self.productID = productID
        self.stop = stop 
        self.stop_price = stop_price

    def Stop_loss(self):
        stopper = reqs.post('https://pro.coinbase.com/orders')
        print(stopper)