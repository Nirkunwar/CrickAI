from flask import Flask, render_template

app = Flask(__name__)

# Data for training modules
SHOTS_DATA = [
    {
        "id": "defense",
        "title": "The Forward Defense",
        "description": "The foundation of a solid batting technique.",
        "steps": [
            "Lean into the line of the ball.",
            "Bring the bat down vertically with a soft grip.",
            "Ensure your head is over the ball at the point of contact."
        ]
    },
    {
        "id": "cover-drive",
        "title": "The Cover Drive",
        "description": "A classic shot played through the off-side.",
        "steps": [
            "Step toward the pitch of the ball.",
            "Transfer weight to the front foot.",
            "Swing the bat through the line toward the covers."
        ]
    },
    {
        "id": "pull-shot",
        "title": "The Pull Shot",
        "description": "Dominating short-pitched bowling.",
        "steps": [
            "Identify the short length early.",
            "Pivot on the back foot and clear your front leg.",
            "Roll your wrists to keep the ball on the ground."
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/training')
def training():
    return render_template('training.html', shots=SHOTS_DATA)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
