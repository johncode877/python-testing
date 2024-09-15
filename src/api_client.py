import requests
import ipaddress

def get_location(ip):
    
    ipaddress.ip_address(ip)
    url = f"https://freeipapi.com/api/json/{ip}"

    response = requests.get(url)
    print(response.status_code)
    print(response.raise_for_status())
    data = response.json()
    
    #import ipdb; ipdb.set_trace()

    return {
        "country":data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"]
    }
    



if __name__ == "__main__":
   print(get_location("300.8.8.8"))