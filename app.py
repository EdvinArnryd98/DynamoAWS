from flask import Flask, render_template
from dynamo import get_table_content

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html', readings=get_table_content())


if __name__ == '__main__':
    app.run()