from flask import Flask, render_template, request, jsonify
import iris_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        sepal_length = request.form['sepallength']
        sepal_width = request.form['petalwidth']
        petal_length = request.form['petallength']
        petal_width = request.form['petalwidth']

        # Check if any of the fields is empty
        if not sepal_length or not sepal_width or not petal_length or not petal_width:
            return jsonify({'error': 'Please enter values for all fields'})

        y_pred = [[float(sepal_length), float(sepal_width), float(petal_length), float(petal_width)]]
        trained_model = iris_model.training_model()
        prediction_value = trained_model.predict(y_pred)

        setosa = 'The flower is classified as Setosa'
        versicolor = 'The flower is classified as Versicolor'
        virginica = 'The flower is classified as Virginica'

        if prediction_value == 0:
            return render_template('index.html', setosa=setosa)
        elif prediction_value == 1:
            return render_template('index.html', versicolor=versicolor)
        else:
            return render_template('index.html', virginica=virginica)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
