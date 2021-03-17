## restApiParsesr

Toolboox for comand line communication with REST APi-s.

### mac_parser.py

Script which enable getting info from macaddress.io api.
Provide mac address and this script give you name of vendor of this address

Example usage using docker:

```
sudo docker build -t mac-parser .
sudo docker run -it mac-parser mac_parser.py -m 44:38:39:ff:ef:57
```

