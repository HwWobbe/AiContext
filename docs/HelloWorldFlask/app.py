from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Hello World</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background: #f4f7fb;
            color: #1f2937;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
          }
          .card {
            background: white;
            padding: 2rem 3rem;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
            text-align: center;
          }
          h1 {
            margin-bottom: 0.5rem;
          }
          p {
            margin: 0;
            color: #4b5563;
          }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>Hello, World!</h1>
          <p>This is a persistent local Flask app.</p>
        </div>
      </body>
    </html>
    """)

@app.route("/api/hello")
def hello_api():
    return jsonify({
        "message": "Hello, World!",
        "status": "ok",
        "app": "persistent-local-flask"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
