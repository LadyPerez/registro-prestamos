from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

loans = []

form_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Préstamo</title>
    <style>
        body {
            background-color: #5DA6A7;
            font-family: Arial, sans-serif;
            color: #333333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #66CAD0;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h1 {
            text-align: center;
            color: #333333;
        }
        label {
            font-weight: bold;
            margin-top: 10px;
            display: block;
        }
        input[type="text"],
        input[type="number"],
        input[type="date"] {
            width: calc(100% - 20px);
            padding: 8px;
            margin-top: 5px;
            border-radius: 5px;
            border: 1px solid #cccccc;
            font-size: 16px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #333333;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 15px;
        }
        input[type="submit"]:hover {
            background-color: #444444;
        }
        h2 {
            text-align: center;
            margin-top: 20px;
            color: #333333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 5px;
            background-color: #ffffff;
            margin-top: 5px;
            border-radius: 5px;
            box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Registro de Préstamo</h1>
        <form action="{{ url_for('register_loan') }}" method="post">
            <label for="borrower">Nombre del Prestatario:</label>
            <input type="text" id="borrower" name="borrower" required><br><br>

            <label for="amount">Monto del Préstamo:</label>
            <input type="number" id="amount" name="amount" required><br><br>

            <label for="date">Fecha del Préstamo:</label>
            <input type="date" id="date" name="date" required><br><br>

            <input type="submit" value="Registrar Préstamo">
        </form>

        <h2>Préstamos Registrados</h2>
        <ul>
        {% for loan in loans %}
            <li>{{ loan['borrower'] }} - {{ loan['amount'] }} - {{ loan['date'] }}</li>
        {% endfor %}
        </ul>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(form_template, loans=loans)

@app.route('/register', methods=['POST'])
def register_loan():
    borrower = request.form['borrower']
    amount = request.form['amount']
    date = request.form['date']

    loans.append({
        'borrower': borrower,
        'amount': amount,
        'date': date
    })

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
