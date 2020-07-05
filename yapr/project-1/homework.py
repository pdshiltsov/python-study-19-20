import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        
    def add_record(self, record):
        self.records.append(record)
    
    def get_today_stats(self):
        remained = 0
        for record in self.records:
            if record.date == dt.date.today():
                remained += record.amount
        return remained

    def get_today_remained(self):
        return self.limit - self.get_today_stats()
    
    def get_week_stats(self):
        wasted_sum = 0.0     

        for record in self.records:
            date_from = (dt.datetime.now() - dt.timedelta(days = 7)).date()
            date_till = dt.date.today()
            
            if date_from <= record.date <= date_till:
                wasted_sum += record.amount
        return wasted_sum
            
class Record:
    def __init__(self, amount = 0, comment = '', date = ''):
        if date == '':
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
            
        self.amount = amount
        self.comment = comment
        
        
    
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):      
        if self.get_today_remained() > 0:
            return("Сегодня можно съесть что-нибудь ещё, " 
                + "но с общей калорийностью не более {} кКал"\
                  .format(self.get_today_remained()))
        else: 
            return('Хватит есть!')
            
class CashCalculator(Calculator): 
    USD_RATE = 60.0
    EURO_RATE = 70.0
    
    def get_today_cash_remained(self, currency):
        rates = {'rub' : [1.0, 'руб'], 'usd' : [self.USD_RATE, 'USD'], 'eur' : [self.EURO_RATE, 'Euro']}
        if currency in rates.keys():            
            remained = self.get_today_remained()
            money = round(remained / rates[currency][0], 2)

            if remained > 0: 
                return ('На сегодня осталось {} {}'.format(money, rates[currency][1])) 
        
            elif remained == 0: 
                return ('Денег нет, держись') 
    
            elif remained < 0: 
                return ('Денег нет, держись: твой долг - {} {}'.format(abs(money),rates[currency][1])) 

