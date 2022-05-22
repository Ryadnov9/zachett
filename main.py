import requests
import csv

region = str(input("Введіть код регіона: "))
codes1 = [12, 14, 18, 21, 23, 26, 32, 35, 44, 46, 48, 51, 53, 56, 59,
          61, 63, 65, 68, 71, 73, 74, 80, 85]
codes2 = ['01', '05', '07']
x = int(region) in codes1
c = int(region) in codes2
if c is False:
    if x is False:
        print('Введіть інший код:')

r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=' + region + '&exp=json')

print('З роком заснування між :' '1950 та 1999')
value = str(input("Вибиріть одине із значень:"))

universities: list = r.json()
filtered_data = [{k: row[k] for k in ['university_id', 'post_index']} for row in universities]
filtered_data2 = [{k: row[k] for k in ['university_name',
                                       'university_name_en',
                                       'university_director_post',
                                       'university_email',
                                       'registration_year']}
                  for k in ['registration_year'] for row in universities if row[k] == value]

with open('universities_' + region + '.csv', mode='w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

with open('rectors.csv', mode='w', encoding='UTF-8') as f1:
    writer = csv.DictWriter(f1, fieldnames=filtered_data2[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data2)
