from Constants import urls


class FMQuery:

    def __init__(self, query='mr2', min_price=850, max_price=5000):
        self.max_price = max_price
        self.min_price = min_price
        self.query = query

    def get_url(self):
        result = ''
        if self . max_price != None and self . min_price:
            result = 'min_price='+str(self.min_price) + \
                '&max_price'+str(self.max_price)
        result = result + '&sortBy=creation_time_descend&exact=false'
        if self . query != None:
            result = result + '&query='+self.query

        return urls.mp_base.format(result)