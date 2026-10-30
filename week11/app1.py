from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    num1 = ""
    num2 = ""

    if request.method == 'POST':
        try:
            num1 = request.form.get('num1', '')
            num2 = request.form.get('num2', '')

            # Determine which button was clicked based on its ID
            if 'add' in request.form:
                result = float(num1) + float(num2)
            elif 'sub' in request.form:
                result = float(num1) - float(num2)
            elif 'mul' in request.form:
                result = float(num1) * float(num2)
            elif 'div' in request.form:
                result = float(num1) / float(num2)

            # Remove trailing .0 for whole numbers so text == "15" not "15.0"
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            else:
                result = round(result, 4)

        except (ValueError, ZeroDivisionError):
            result = "Error"

    return render_template(
        'calculator.html',
        result=result,
        num1=num1,
        num2=num2
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50011, debug=True)