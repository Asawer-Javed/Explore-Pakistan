from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def main_page():
    return render_template('index.html')

@application.route('/Home')
def sub_page1():
    return render_template('pages/home.html')

@application.route('/Culture')
def sub_page2():
    return render_template('pages/culture.html')

@application.route('/Economy')
def sub_page3():
    return render_template('pages/economy.html')

@application.route('/Explore Cities')
def sub_page4():
    return render_template('pages/explore_cities.html')

@application.route('/Geography')
def sub_page5():
    return render_template('pages/geography.html')

@application.route('/History')
def sub_page6():
    return render_template('pages/history.html')

@application.route('/Islamabad')
def sub_page7():
    return render_template('pages/islamabad.html')

@application.route('/Karachi')
def sub_page8():
    return render_template('pages/karachi.html')

@application.route('/Multan')
def sub_page9():
    return render_template('pages/multan.html')

if __name__ == "__main__":
    application.run(debug=True)