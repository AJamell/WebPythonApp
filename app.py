from flask import Flask, request
import os

app = Flask(__name__)

def read_count():
    try:
        with open('data/count.txt', 'r') as f:
            count = int(f.read())
        return count
    except IOError:
        return 0

def save_count(count):
    os.makedirs('data', exist_ok=True)
    with open('data/count.txt', 'w') as f:
        f.write(str(count))

@app.route("/", methods=['GET', 'POST'])
def hello():
    count = read_count()
    count += 1
    save_count(count)
    
    name = "Guest"
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
    
    return """
    <html>
    <body>
        <h1 style='color:red'>Hello, {}! Visitor count: {}</h1>
        <form method='post'>
            <input type='text' name='name' placeholder='Enter your name'>
            <button type='submit'>Submit</button>
        </form>
    </body>
    </html>
    """.format(name, count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

