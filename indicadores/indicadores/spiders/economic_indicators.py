import scrapy
from indicadores.items import Producto
import datetime

class EconomicIndicators(scrapy.Spider):
    """ Spider para obtener nuestra data"""
    name = 'e_indicators'
    start_urls = [
        'https://www.exito.com/multicooker-11-en-1-digital-6l-479689/p',
        'https://www.exito.com/olla-arrocera-inox-con-vaporer-finlandek-fi75078-397450/p',
        'https://www.exito.com/olla-apresion-multichef-pro-imusa-ce753856-3039728/p',
        'https://www.exito.com/olla-multifuncional-blackdecker-5-litros-mc21850-robot-de-cocina-negro-102052616-mp/p',
        'https://www.exito.com/olla-arroz-gris-20t-630631/p'
    ]

    custom_settings = {
        'FEED_URI': 'exito.csv',
        'FEED_FORMAT': 'csv',
        'ROBOTSTXT_OBEY': True,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        producto = Producto()


        producto['nombre'] = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        producto['valor'] = response.xpath('//meta[@property="product:price:amount"]/@content').extract_first()
        producto['sku'] = response.xpath('//meta[@property="product:sku"]/@content').extract_first()
        producto['imagen'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
        producto['descripcion'] = response.xpath('//meta[@property="og:description"]/@content').extract_first()
        producto['modelo'] = response.xpath('//div[contains(@class,"exito-product-details-3-x-specificationsNlTwo w-100")]/text()').extract_first()
        producto['marca'] = response.xpath('//meta[@property="product:brand"]/@content').extract_first()
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
        