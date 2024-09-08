from app import app

# this is the run file 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)
