import re
from typing import Tuple


def get_pep_name_and_number(pep_discription: str) -> Tuple[str, str]:
    """Получение номера документа Pep и его названия."""

    pattern_pep_name = r"(?<=– )[\w \S]*$"
    pattern_pep_num = r"(?<=PEP )[\d]*"
    number = re.search(pattern_pep_num, pep_discription).group()
    name = re.search(pattern_pep_name, pep_discription).group()
    return number, name
