# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class MyprojectPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("kiko_milano.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS kiko_milano""")
        self.curr.execute("""create table kiko_milano(
                            name text,
                            data_product text,
                            action text,
                            service text,
                            link text
                        )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute("""insert into kiko_milano values (?,?,?,?,?)""",(
            item['name'][0],
            item['data_product'][0],
            item['action'][0],
            item['service'][0],
            'https://www.kikomilano.com.tr'+item['link'][0]
        ))
        self.conn.commit()
