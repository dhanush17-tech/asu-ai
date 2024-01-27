from embedchain import App
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

asuApp = App()
# asuApp.add('https://tuition.asu.edu/sitemap.xml', data_type='sitemap')
# asuApp.add('https://fullcircle.asu.edu/faculty-sitemap.xml', data_type='sitemap')
# asuApp.add('https://fullcircle.asu.edu/external_news-sitemap.xml', data_type='sitemap')
# asuApp.add('https://asu.campuslabs.com/engage/api/discovery/search/organizations?orderBy%5B0%5D=UpperName%20asc&top=100&filter=&query=&skip=70', data_type='sitemap')
asuApp.online = True

doYouWantToContinue='y'

doYouWantToContinue = input("Do you want to continue? (y/n) ")
while doYouWantToContinue == 'y':
    prompt = input("Ask me anything ASU stuff! 🔱 ")

    print(asuApp.query(prompt))
    
    doYouWantToContinue = input("Do you want to continue? (y/n) ")

    