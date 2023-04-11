from datetime import datetime
class CarAD:

    def __init__(self, desc, url):
        self.price = desc[0]
        self.url = url
        self.date = datetime.now()
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

        try:
            end_index = url.index('/?ref')
            self.uid = url[start_index:end_index]
        except ValueError:
            self.uid = url[start_index:]

    def set_images(self, img, img_src):
        self.img = img
        self.img_src = img_src

    def to_dict(self):
        return {
            'uid': self.uid,
            'title': self.title,
            'km': self.km,
            'location': self.location,
            'date': self.date,
            'price': self.price,
            'url': self.url,
            'img_data': self.img,
            'img_src': self.img_src,
            "metadata": {"width": 800, "height": 600},
        }

    def to_string(self):
        result = '⚠️⚠️⚠️⚠️⚠️⚠️\n<b>! Nuevo anuncio publicado !</b>\n ⚠️⚠️⚠️⚠️⚠️⚠️\n\n\n' + self.title + '\n 📏<b>KMs</b> ' + \
            self.km + '\n📍<b>Localizacion</b> : ' + self.location + \
            '\n 💰<b>Precio</b> ' + self.price + '\n\n\n 🔗<b>Link</b> : ' + self.url
        return result
