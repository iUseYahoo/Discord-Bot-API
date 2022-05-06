from flask import *
import sqlite3, os
from bs4 import BeautifulSoup
connection = sqlite3.connect('./Database/main.db', check_same_thread=False)
cursor = connection.cursor()

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

app = Flask(__name__)

portnum = 8888

###########################################
# Home Page                               #
###########################################
@app.route('/', methods=['GET'])
def home_page():
    show_welcome = {'Welcome to the home page'}

    return str(show_welcome).replace('{', '').replace('}', '').replace("'", '')

###########################################
# Dictionary DB Page                      #
###########################################
@app.route('/dictionary/', methods=['GET'])
def dictionary():
    get_word = request.args.get('word').lower()

    bad_sql = open('../bad_sql.txt', 'r')

    for line in bad_sql:
        if get_word in line:
            bad_sql.close()
            embed = '<div class="tenor-gif-embed" data-postid="16929018" data-share-method="host" data-aspect-ratio="1.50943" data-width="50%"><a href="https://tenor.com/view/facepalm-double-crowd-funny-omg-gif-16929018">Facepalm Double GIF</a>from <a href="https://tenor.com/search/facepalm-gifs">Facepalm GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>'

            return "You're a bad person, But nice try." + embed 

    if get_word is None:
        return "Please enter a word"
    else:
        cursor.execute("SELECT meaning FROM dictionary WHERE word = ?", (get_word,))
        result = cursor.fetchone()

        if result is None:
            return "Sorry, that word is not in the dictionary"
        else:
            return str(result).replace('(', '').replace(')', '').replace("'", '')

        
###########################################
# Pull information on a IP from Whoi.is   #
###########################################
@app.route('/whois/', methods=['GET'])
def whoisv1():
    entered_ip = request.args.get("ip")
    whois_url = f'https://who.is/whois-ip/ip-address/{entered_ip}'

    if entered_ip == "":
        return "Please enter an IP address."
    else:
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

        # get the value of class airT
        site = requests.get(whois_url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        whoisResult = soup.find(class_='col-md-12 queryResponseBodyKey')

        if whoisResult is None:
            return "No results found."
        else:
            return whoisResult.prettify()


if __name__ == '__main__':
    # write the portnum into the config.json file
    with open('../config.json', 'r+') as json_file:
        data = json.load(json_file)
        data['port'] = int(portnum)
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()
        json_file.close()

    app.run(port=portnum)

