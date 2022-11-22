import scrapy
import pandas 
from indicadores.items import Producto
from indicadores.PropertieController import *
from indicadores.DBUpDown import *
import datetime
load_dotenv()

countries = eval(get_countries())
retailers = eval(get_retailers())
dataframe = GetDataFrame('product_homologated','psql_read').get_dataframe
dataframe = dataframe[dataframe['PAIS'].isin(countries)]
dataframe = dataframe[dataframe['RETAILER'].isin(retailers)]
print (dataframe)

class EconomicIndicators(scrapy.Spider):
    """ Spider para obtener nuestra data"""
    name = 'e_indicators'
    start_urls = 
    
"""    start_urls = [
        'https://www.exito.com/multicooker-11-en-1-digital-6l-479689/p',
        'https://www.exito.com/olla-arrocera-inox-con-vaporer-finlandek-fi75078-397450/p',
        'https://www.exito.com/olla-apresion-multichef-pro-imusa-ce753856-3039728/p',
        'https://www.exito.com/olla-multifuncional-blackdecker-5-litros-mc21850-robot-de-cocina-negro-102052616-mp/p',
        'https://www.exito.com/olla-arroz-gris-20t-630631/p'
    ]"""

    custom_settings = {
        'FEED_URI': 'exito.csv',
        'FEED_FORMAT': 'csv',
        'ROBOTSTXT_OBEY': True,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        producto = Producto()

        producto['PAIS'] = 'PAIS'
        producto['CATEGORIA'] = 'CATEGORIA'
        producto['SUBCATEGORIA'] = 'SUBCATEGORIA'
        producto['WEB_NAME'] = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        producto['RETAILER'] = 'RETAILER'
        producto['URL'] = response.xpath('NULL')
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
        producto['fecha'] = datetime.date.today()

        yield producto


''' 

        info = {
                'nombre': nombre,
                'valor': valor,
                'sku': sku,
                'imagen':imagen,
                'descripcion':descripcion,
                'modelo':modelo,
                'marca':marca,
                'fecha': datetime.date.today()
            }

        yield info
        

        
   
        for ind, val in zip(indicators, values):
            info = {
                'nombre': ind,
                'valor': val,
                'fecha': datetime.date.today()
            }

            yield info
 '''
        