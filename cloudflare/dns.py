#!/usr/bin/python3
import requests
import json

class CloudFlareDns():
    def __init__(self, auth_email, auth_key, zone_id):
        """ Constructor
        :type file: str
        :param auth_email: Authentication email

        :type section: str
        :param: auth_key: Authentication API key

        :type section: str
        :param: zone_id: Zone ID in claredflare to alter records in
        """
        self.endpoint = "https://api.cloudflare.com/client/v4/"
        self.zone_id = zone_id
        self.headers = {
            'X-Auth-Email': auth_email,
            'X-Auth-Key': auth_key,
            'Content-Type': 'application/json'
        }

    def get_dns_record(self, record_name):
        """ get_dns_record
        :type file: str
        :param record_name: Record name in Cloudflare to update

        :type file: str
        :param record_value: Record value in Cloudflare to update
        """
        url = self.endpoint + 'zones/' + self.zone_id + '/dns_records/?&match=all&name=' + record_name
        conn = requests.session()

        try:
            req = conn.get(url, headers=self.headers)
        except (requests.ConnectionError) as err:
            print(err)
            return False
        else:
            data = json.loads(req.content)
            return data

    def create_dns_record(self, record_name, record_value, record_type):
        """ create_dns_record
        :type file: str
        :param record_name: Record name in Cloudflare to create

        :type file: str
        :param record_type: Record type in Cloudflare to create, I.E 'A'

        :type file: str
        :param record_value: Record value in Cloudflare to create
        """
        url = self.endpoint + 'zones/' + self.zone_id + '/dns_records'
        data = {
            "type": record_type,
            "name": record_name,
            "content": record_value,
            "ttl": 1,
            "priority": 10,
            "proxied": False
        }
        json_data = json.dumps(data)
        json_data = json_data.encode('utf-8')
        conn = requests.session()

        try:
            req = conn.post(url, data=json_data, headers=self.headers)
        except (requests.ConnectionError) as err:
            print(err)
        else:
            print("INFO: Record " + record_name + " has been successfully added.")
            return req.content

    def update_dns_record(self, record_name, record_value, record_type):
        """ update_dns_record
        :type file: str
        :param record_name: Record name in Cloudflare to update

        :type file: str
        :param record_value: Record value in Cloudflare to update

        :type file: str
        :param record_type: Record type in Cloudflare this should match existing record type, I.E 'A'
        """
        url = self.endpoint + 'zones/' + self.zone_id + '/dns_records/'
        new_data = {
            "type": record_type,
            "name": record_name,
            "content": record_value
        }
        json_data = json.dumps(new_data)
        json_data = json_data.encode('utf-8')

        conn = requests.session()

        existing_data = self.get_dns_record(record_name)

        if (existing_data['result']):
            url = url + existing_data['result'][0]['id']
            try:
                req = conn.put(url, data=json_data, headers=self.headers)
            except (requests.ConnectionError) as err:
                print(err)
            else:
                print("INFO: Record " + record_name + " has been successfully updated.")
                return req.content
        else:
            print("ERROR: Record " + record_name + " doesn't exist, please create one first.")

    def delete_dns_record(self, record_name):
        """ delete_dns_record
        :type file: str
        :param record_name: Record name in Cloudflare to delete
        """
        url = self.endpoint + 'zones/' + self.zone_id + '/dns_records/'

        conn = requests.session()

        record = self.get_dns_record(record_name)

        if (record['result']):
            url = url + record['result'][0]['id']
            try:
                req = conn.delete(url, headers=self.headers)
            except (requests.ConnectionError) as err:
                print(err)
            else:
                print("INFO: Record " + record_name + " has been successfully deleted.")
                return req.content
        else:
            print("ERROR: Record " + record_name + " doesn't exist, or has already been deleted.")