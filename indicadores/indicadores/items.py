# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class Producto(scrapy.Item):

    nombre = scrapy.Field()
    valor = scrapy.Field()
    sku = scrapy.Field()
    imagen = scrapy.Field()
    descripcion = scrapy.Field()
    modelo = scrapy.Field()
    marca = scrapy.Field()
    fecha = scrapy.Field()  



