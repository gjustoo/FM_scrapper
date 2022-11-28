class CarAD:

    def __init__(self, desc, url):
        self.price = desc[0]
        self.url = url
        self.__process_uid()
        if len(desc) == 5:
            self.title = desc[2]
            self.location = desc[3]
            self.km = desc[4]
        elif len(desc) == 3:
            self.title = desc[1]
            self.location = desc[2]
        else:
            self.title = desc[1]
            self.location = desc[2]
            self.km = desc[3]

    def __process_uid(self):

        url = self.url

        start_index = url.index('item/') + len('item/')
        end_index = url.index('/?hoi')

        self.uid = url[start_index:end_index]
