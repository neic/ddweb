from adaptor.model import CsvModel
from adaptor.fields import CharField, DateField
from ddweb.apps.news.models import Article


class NewsImporter(CsvModel):
    headline = CharField()
    date = DateField(**{"format": "%d/%m/%Y %H:%M:%S"})
    description = CharField()
    author = CharField()

    class Meta:
        delimiter = ";"
        dbModel = Article


csvlist = NewsImporter.import_data(data=open("news-nopic.csv"))
