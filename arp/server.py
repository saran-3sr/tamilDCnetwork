mac_ip={
    '10.2.2.5':'00:16:2e:99:0b:db',
    '10.5.5.5':'00:16:4e:99:0b:db'
}
import requests
url='http://ptsv2.com/t/kbyg8-16668/post'
r=requests.post(url,data=mac_ip)
print(r)