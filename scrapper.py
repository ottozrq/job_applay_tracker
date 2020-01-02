import requests
from bs4 import BeautifulSoup

from config import app


class LinkedinScrapper:
    login_page = 'https://www.linkedin.com/uas/login-submit'
    login_email = app.config['LINKEDIN_USER']
    login_password = app.config['LINKEDIN_PASS']
    session = None

    def __init__(self):
        payload = {
            'session-key': self.login_email,
            'session-password': self.login_password
        }
        s = requests.session()
        s.post(self.login_page, data=payload)
        self.session = s

    def parse(self, url):
        body = self.session.get(url).text
        soup = BeautifulSoup(body, 'html.parser')
        result = self.find_basic_info(soup, url)
        return result

    @staticmethod
    def find_basic_info(soup, url):
        result = dict()
        result['url'] = url
        div = soup.find('div', {'class': 'topcard__content-left'})
        title = div.find('h1', {'class': 'topcard__title'})
        result['title'] = title.string
        company = div.find('a', {'class': 'topcard__org-name-link topcard__flavor--black-link'})
        result['company'] = company.string
        location = div.find('span', {'class': 'topcard__flavor topcard__flavor--bullet'})
        result['location'] = location.string
        publish_date = div.find('span', {'class': 'topcard__flavor--metadata posted-time-ago__text'})
        if publish_date:
            result['publish_date'] = publish_date.string
        else:
            result['publish_date'] = '0 days ago'
        content = soup.find('div', {'class': 'description__text description__text--rich'})
        result['content'] = content
        return result


if __name__ == '__main__':
    html = 'https://www.linkedin.com/jobs/view/1621025764'
    ls = LinkedinScrapper()
    res = ls.parse(html)
    print(res)


