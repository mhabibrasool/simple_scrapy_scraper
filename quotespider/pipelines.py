# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotePipeline:
    def process_item(self, item, adapter):
        adapter = ItemAdapter(item)
        
        
        # Strip all white spaces from 'Title'
        title = adapter.get('Title')
        adapter['Title'] = title.strip()
        
        # Strip all white space from  'author'
        author = adapter.get('Author')
        adapter['Author'] = author.strip()
        
        return item