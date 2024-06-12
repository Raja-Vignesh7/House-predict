from flask import Flask, render_template, request , jsonify
import joblib
import traceback
app = Flask(__name__,template_folder='pages',static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_price', methods=['GET'])
def calculate_price():
    model = joblib.load('Hp_model')
    try:
        area = int(request.args.get('area'))
        # print(area)
        #return jsonify({'price':area})
        if area:
            price = model.predict([[area]])[0]
            #price = area*100
            return jsonify({'price': round(price,2)})
        return jsonify({'error': 'Invalid input'})
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()  # This will print the error stack trace to the console
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(port=3000,debug=True)