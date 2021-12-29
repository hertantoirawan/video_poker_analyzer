from flask import Flask
from vp_analyzer import HandAnalyzer

app = Flask(__name__)

@app.route("/analyze/<hand>")
def analyze_api(hand):
    response = HandAnalyzer(hand).analyze(return_full_analysis=False, return_bestdisc_cnts = True)
    return response

@app.errorhandler(404)
def page_not_found(error):
    response = "<p>Use /analyze/&lthand&gt </p><p>Hands are represented as 10-character long strings, with a card rank character followed by a suit character. The expected rank characters are: A, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K. The expected suit characters are: c, d, h, s. When dealing with discards, cards to be replaced are represented by 'XX'. For example, a hand containing: Three of Clubs, Ace of Hearts, Three of Diamonds, Ten of Hearts, Jack of Spades; is '3cAh3dThJs' and one discard strategy would be to hold the pair of threes: '3cXX3dXXXX'.</p>"
    return response    
    