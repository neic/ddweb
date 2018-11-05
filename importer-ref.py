from adaptor.model import CsvDbModel
from ddweb.apps.references.models import Reference


class RefImporter(CsvDbModel):
    class Meta:
        delimiter = ";"
        dbModel = Reference


csvlist = RefImporter.import_data(data=open("ref.csv"))
