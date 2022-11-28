import scrapy
import pandas as pd
from indicadores.PropertieController import df_get
from indicadores.items import Producto
from indicadores.PropertieController import *
from indicadores.DBUpDown import *
import datetime

class EconomicIndicators(scrapy.Spider):
    """ Spider para obtener nuestra data"""
    name = 'e_indicators'

    def stock_list():
            start_urls = []
            for i, df in df_get().iterrows():
                start_urls.append(df['URL'])
            return start_urls

    start_urls = stock_list()

    custom_settings = {
        'FEED_URI': 'exito.csv',
        'FEED_FORMAT': 'csv',
        'ROBOTSTXT_OBEY': True,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        producto = Producto()

        producto['PAIS'] = 'none' # str(df['PAIS'])
        producto['CATEGORIA'] = 'none' # str(df['CATEGORIA'])
        producto['SUBCATEGORIA'] = 'none' # str(df['SUBCATEGORIA'])
        producto['WEB_NAME'] = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        producto['RETAILER'] = 'none' # str(df['RETAILER'])
        producto['URL'] = 'none' # str(df['URL'])
        producto['DESCRIPTIONB'] = response.xpath('//meta[@property="og:description"]/@content').extract_first()
        producto['PRICE'] = response.xpath('//meta[@property="product:price:amount"]/@content').extract_first()
        producto['DESCRIPTIONF'] = response.xpath('NULL')
        producto['SKU'] = response.xpath('//meta[@property="product:sku"]/@content').extract_first()
        producto['SEGMENTO4'] = response.xpath('NULL')
        producto['MARCA'] = response.xpath('//meta[@property="product:brand"]/@content').extract_first()
        producto['MODELO_RETAILER'] = response.xpath('//div[contains(@class,"exito-product-details-3-x-specificationsNlTwo w-100")]/text()').extract_first()
        producto['IMAGE'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
        producto['ROW_ID'] = 0
        producto['CYCLE_ID'] = 0
        producto['SEGMENTO1'] = 'NULL'
        producto['SEGMENTO2'] = 'NULL'
        producto['SEGMENTO3'] = 'NULL'
        producto['SEGMENTO5'] = 'NULL'
        producto['MODELO_HITCH'] = 'none' # str(df['MODELO HITCH'])
        producto['fecha'] = datetime.date.today()

        yield producto


