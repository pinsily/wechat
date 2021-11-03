from typing import Dict

import xmltodict

from settings import logger
from utils.str_utils import hump2underline


def xml_to_dict(xml_str: str) -> Dict:
    """
    xml str to unline key dict
    :param xml_str:
    :return:
    """
    logger.info(f"xml_to_dict req=>{xml_str}")
    xml_dict = dict()
    doc = xmltodict.parse(xml_str)["xml"]
    for key, value in doc.items():
        xml_dict.__setitem__(hump2underline(key), value)

    logger.info(f"xml_to_dict resp=>{xml_dict}")
    return xml_dict
