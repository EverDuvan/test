# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class Producto(scrapy.Item):

    fecha = scrapy.Field()

    PAIS = scrapy.Field()
    CATEGORIA = scrapy.Field()
    SUBCATEGORIA = scrapy.Field()
    WEB_NAME = scrapy.Field()
    RETAILER = scrapy.Field()
    URL = scrapy.Field()
    DESCRIPTIONB = scrapy.Field()
    PRICE = scrapy.Field()
    DESCRIPTIONF = scrapy.Field()
    SKU = scrapy.Field()
    SEGMENTO4 = scrapy.Field()
    MARCA = scrapy.Field()
    MODELO_RETAILER = scrapy.Field()
    IMAGE = scrapy.Field()
    ROW_ID = scrapy.Field() # 0
    CYCLE_ID = scrapy.Field() # 0
    SEGMENTO1 = scrapy.Field() # 'NULL'
    SEGMENTO2 = scrapy.Field() # 'NULL'
    SEGMENTO3 = scrapy.Field() # 'NULL'
    SEGMENTO5 = scrapy.Field() # 'NULL'
    MODELO_HITCH = scrapy.Field()
