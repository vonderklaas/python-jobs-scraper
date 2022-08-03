from bs4 import BeautifulSoup
import requests

domain_name = 'https://relocate.me'

print('Welcome to Jobs scraper!')

desired_skill = input('Enter your strongest skill: ')
is_write = input('Save jobs in separate files? [y/n]: ').lower()

print('I am looking for matching jobs!')

def find_jobs():
    html_text = requests.get(f'https://relocate.me/search?query%5B%5D={desired_skill}').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='jobs-list__job')

    for index, job in enumerate(jobs):
        more = job.a['href']
        position = job.a.b.text
        country = job.a.text.split()[-1]
        company = job.find('div', class_='job__company').text.strip()
        skills_object = job.find_all('span', class_='job__tag')
        skills = []

        for skill in skills_object:
            skills.append(skill.text)

        if is_write == 'y':
            # Write to file
            with open(f'posts/{index}.txt', 'w') as file:
                file.write(f'Position: {position} \n')
                file.write(f'Country: {country} \n')
                file.write(f'Company: {company} \n')
                file.write(f'Skills: {skills} \n')
                file.write(f'More: {domain_name + more} \n')

        print(f'''
            Position: {position}
            Country: {country}
            Company: {company}
            Skills: {skills}
            More: {domain_name + more}
        ''')

find_jobs()