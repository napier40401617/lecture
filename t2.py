from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('t2.html',name=name)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5004, debug=True)