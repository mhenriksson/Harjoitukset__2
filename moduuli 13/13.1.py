from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku')
def alkuluku(luku):

    luku = int(luku)
    alkuluku = True
    for x in range(2, luku):
        if luku % x == 0:
            alkuluku = False
            break

    v = {
        "Number" : luku,
        "isPrime" : alkuluku
    }



    return v

app.run(use_reloader=True, host='127.0.0.1', port=3000)