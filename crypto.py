import requests

print(""" ______     ______     __  __     ______   ______   ______    
/\  ___\   /\  == \   /\ \_\ \   /\  == \ /\__  _\ /\  __ \   
\ \ \____  \ \  __<   \ \____ \  \ \  _-/ \/_/\ \/ \ \ \/\ \  
 \ \_____\  \ \_\ \_\  \/\_____\  \ \_\      \ \_\  \ \_____\ 
  \/_____/   \/_/ /_/   \/_____/   \/_/       \/_/   \/_____/ 
                                                              """)
print("instagram:iq4.p")
print("made by yahya")
print("team t10s")
print("github:yahya778")


r = requests.get(input("enter api url:"))
r = r.json()
usd = r['USD']
eur = r['EUR']
print("usd=")
print (usd)
print("euro=")
print(eur)
    
    
    