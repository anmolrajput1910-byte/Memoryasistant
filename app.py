from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

def search_notes(query):
    return [n for n in notes if query.lower() in n.lower()]

def answer_from_notes(query):
    for n in notes:
        if query.lower() in n.lower():
            return n
    return "No answer found."

@app.route("/", methods=["GET", "POST"])
def home():
    result = {}
    
    if request.method == "POST":
        action = request.form["action"]
        
        if action == "add":
            note = request.form["note"]
            notes.append(note)
            result["message"] = "Note added"

        elif action == "search":
            query = request.form["query"]
            result["search"] = search_notes(query)

        elif action == "ask":
            query = request.form["query"]
            result["answer"] = answer_from_notes(query)

    return render_template("index.html", notes=notes, result=result)

if __name__ == "__main__":
    app.run(debug=True)