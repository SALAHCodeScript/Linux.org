#!/usr/bin/python3.13
import http.client

conn = http.client.HTTPSConnection("www.google.com")
conn.request("GET", "/")
response = conn.getresponse()

print(response.status, response.reason)
print(response.read().decode())
