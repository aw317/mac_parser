import argparse
import os
import sys
import warnings
import yaml

from src.connector import ServerApiConnector
from src.passwords import decode_token

warnings.filterwarnings("ignore", category=yaml.YAMLLoadWarning)


class MacAddressParser:
    available_formats = {'vendor'}

    def __init__(self, connector: ServerApiConnector, out_format):
        self.connector = connector
        self.out_format = out_format

    def get_company_name(self, mac_address):
        query = {'output': self.out_format, 'search': mac_address}
        if self.out_format == 'vendor':
            return self.parse_vendor(self.connector.get(query=query))
        else:
            raise NotImplementedError(f'Only {self.available_formats} supported')

    def parse_vendor(self, response):
        if response.status_code == 200:
            return response.text
        else:
            print(f'Error occurred. Received status {response.status_code} and message {response.text}')
            sys.exit(1)


def main(args):
    with open(os.path.join(os.path.dirname(__file__), 'config.yml'), 'r') as conf:
        config = yaml.load(conf)
    endpoint = config['services']['macaddress']['address']
    sec_path = os.path.join(os.path.dirname(__file__), 'secret.bin')

    # decrypt encrypted token from secret.bin file or config
    if os.path.exists(sec_path):
        with open(sec_path, 'rb') as sec:
            token = decode_token(sec.read())
    else:
        token = decode_token(config['services']['macaddress']['token'])
    token_key = config['services']['macaddress']['token_key']
    out_fmt = config['services']['macaddress']['output_format']
    connector = ServerApiConnector(endpoint, token, token_header_key=token_key)
    parser = MacAddressParser(connector, out_fmt)
    print(parser.get_company_name(args.mac_address))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Script should be used to get company name based on mac address")
    parser.add_argument('-m', '--mac_address', help="Address mac used to get a vendor of this address",
                        required=True)
    args = parser.parse_args()
    main(args)
