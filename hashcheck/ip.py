import logging
import ipaddress
from dataclasses import dataclass

from hashcheck import IOC
from hashcheck.services import Shodan, ip_services
from hashcheck.exceptions import InvalidIPException

from shodan.exception import APIError

logger = logging.getLogger(__name__)

f_handler = logging.FileHandler("hashcheck.log")
f_handler.setLevel(logging.INFO)

f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
f_handler.setFormatter(f_format)

logger.addHandler(f_handler)


@dataclass
class IPReport:
    shodan: Shodan = None


class IP(IOC):
    def __init__(self, ip_addr: str):
        self.ioc = None
        self.name = None
        self.reports = None
        self.all_services = ip_services

        try:
            self.ioc = ipaddress.ip_address(ip_addr)
        except ValueError:
            raise InvalidIPException

        if not isinstance(self.ioc, str):
            raise InvalidIPException

        # self.is_ipv4 = True if self.hash_type == SHA256 else False
        # self.is_ipv6 = True if self.hash_type == MD5 else False

    def check(self, services=None, config_path=None):
        reports = None

        try:
            reports = self._get_reports(services, config_path)
        except APIError as e:
            if e == "Invalid IP":
                raise InvalidIPException

        if reports:
            return IPReport(**reports)
        else:
            return None
