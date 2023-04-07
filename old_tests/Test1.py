import requests
import datetime
import asyncio




class Price_detecter():
    def __init__(self, api):
        self.api = api
        self.coin = tuple()
        self.timer = datetime.datetime

    def get_price(self, coin):
        return float(requests.get(self.api+coin).json()["price"])
    
    def get_one_procent_of_coin(self, coin):
        return float(self.get_price(coin)//100)
    
    def create_coin(self, coin):
        self.coin = (coin, self.get_one_procent_of_coin(coin))
    
    async def start_cheking(self):
        while True:
            await asyncio.sleep(1/1000)
            check_price = self.get_price(self.coin[0])
            if check_price < check_price - self.coin[1]:
                print(f"{self.coin[0]} has new price: {check_price}")
                self.create_coin [self.coin[0]]
            if self.timer.now().minute == 0:
                self.create_coin(self.coin)

    async def start_cheking_asincio(self):
        process = loop.create_task(self.start_cheking())
        await asyncio.gather(process)

price_detect = Price_detecter(api='https://api.binance.com/api/v3/avgPrice?symbol=')
price_detect.create_coin("XRPUSDT")
loop = asyncio.get_event_loop()
loop.run_until_complete(price_detect.start_cheking_asincio())

# Что бы реализовать возможность мониторинга нескольких монет, я бы модифицировал метод "create_coin" в 
# метод который добавляет монеты в словарь в котором ключ: Название пары, Значение: цена.
# за тем в цикле While перебирал их, и на каждый запрос создавался бы отдельный Task, т.к.
# запросы в любом случае происходят с достаточной задержкой, то это время было бы логично использовать это время 
# для передачи управления на другой запрос.