import requests
import argparse
import os

url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token {token}".format(token = os.environ['API_TOKEN'])

def upload(file_report, type_scan):
    print("[+] Cargando reporte ...")
    headers = {
        'accept': 'application/json',
        'Authorization': api_key
    }

    report = {
        'file': open(file_report, 'rb')
    }

    body = {
        'product_name': 'WebGoat',
        'engagement_name': 'prueba',
        'product_type_name': 'Research and Development',
        'active': True,
        'verified': True,
        'scan_type': type_scan
    }

    r = requests.post(url_api.format(method = 'import-scan/'), data = body, files = report, headers = headers, verify=False, allow_redirects=False)

    if r.status_code == 201:
        print('[+] Se ha cargado el reporte de {type_scan} con éxito: "{name_report}"'.format(type_scan = type_scan, name_report = file_report))
    else:
        print('[-] Hubo un error al cargar el reporte')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--file', '-f', dest='file', help='Nombre del reporte', required=True)
    parser.add_argument('--type-scan', '-t', dest='type_scan', help='Nombre del escaner', required=True)

    args = parser.parse_args()

    upload(args.file, args.type_scan)
