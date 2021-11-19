from urllib import request as req
from collections import Counter

with req.urlopen('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs') as file:
    base = [line.split()[0] for line in file]

ip, count = Counter(base).most_common(1)[0]
print(f'IP Адресс спамера: {ip.decode("utf-8")}, количество запросов: {count}')

#не виснет, информации много долго идет поиск =)
