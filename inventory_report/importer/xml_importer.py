from inventory_report.importer.importer import Importer
import xml_to_dict


class XmlImporter(Importer):
    def import_data(arq):
        Importer.validate_extension(arq, "xml")
        with open(arq, "r") as content:
            parser = xml_to_dict.XMLtoDict()
            file = content.read()
            result = parser.parse(file)
            result_final = [dict(line) for line in result["dataset"]["record"]]
            return result_final
