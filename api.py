
@app.route('/')
def helloWorld():
    return "<b>bye</b> bye <br/> <p>world</p>"


@app.route('/predict/<x>/<y>')
def anotherFunction(x , y):
    a = int(x)
    b = int(y)
    c = a +b
    return { "result" : str(c) }



app.run("0.0.0.0", port=5001)
