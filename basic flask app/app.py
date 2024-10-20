from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # Route for the home page
    @app.route('/')
    def home():
        return render_template('index.html')

    # Route for the about page
    @app.route('/about')
    def about():
        return render_template('about.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
