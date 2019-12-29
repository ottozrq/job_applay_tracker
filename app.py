from config import app
from scrapper import LinkedinScrapper


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
