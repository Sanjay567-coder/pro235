import requests

for i in range(1, 50000):
    Url = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    r = requests.get(Url)
    if r.status_code == 200:
        print(Url)
    else:
        print("URL not opening")