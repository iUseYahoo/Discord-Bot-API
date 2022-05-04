from flask import *
import sqlite3, os
connection = sqlite3.connect('./Database/main.db', check_same_thread=False)
cursor = connection.cursor()

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

app = Flask(__name__)

#portnum = int(input("What port number would you like to run the server on? "))

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

    bad_sql = open('bad_sql.txt', 'r')

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

if __name__ == '__main__':
    app.run(port=8081)
