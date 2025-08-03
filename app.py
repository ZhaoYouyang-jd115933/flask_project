from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route('/')
def hello_world():
    """Display a simple "Hello World" message on the homepage."""
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Greet the user with their name if provided, or a generic greeting."""
    return f"Hello {name}"


@app.route('/convert/<celsius>')
def convert_temperature(celsius):
    """Convert a Celsius temperature to Fahrenheit and return a formatted string."""
    try:
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"{celsius}°C is {fahrenheit:.2f}°F"
    except ValueError:
        return "Invalid temperature input. Please provide a number."

if __name__ == '__main__':
    app.run(debug=True)
