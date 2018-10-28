# CloudFlare REST API Client
## Overview
A basic Python CloudFlare REST API client library.

So far functuionality is limited to:
* Adding DNS records
* Updating DNS records
* Deleting DNS records

## Usage
Ensure the package is first installed:
```
python3 -m pip install .
```

Examples:
```
from cloudflare.dns import CloudFlareDns
client = CloudFlareDns(
    'blah@something.com',
    'API_KEY',
    'ZONE_ID'
)

client.create_dns_record('example.com', '8.8.8.8', 'A')

client.update_dns_record('example.com', '8.8.6.6', 'A')

client.delete_dns_record('example.com')
```