import get_data as data
import logger as log
import xml_create as xml

log.pohne_logger(xml.xml_create(data.get_info()))