# PYTHON FILE

from flask import *
app = Flask(__name__)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import string
import twitterdata
twitter_handles = twitterdata.twitter_handles
from candidate_tweets import *
import candidate_tweets
from voter_issues import *

global issues
issues = ["abortion", "immigration", "terrorism", "weapons"]
biden = candidate_tweets.biden
bloomberg = candidate_tweets.bloomberg
buttigieg = candidate_tweets.buttigieg
de_la_fuente = candidate_tweets.de_la_fuente
gabbard = candidate_tweets.gabbard
klobuchar = candidate_tweets.klobuchar
sanders = candidate_tweets.sanders
trump = candidate_tweets.trump
warren = candidate_tweets.warren

def get_politician_tweets(politician):
    if politician == "biden":
        total_string=""
        for tweet in biden:
            total_string += str(tweet)
        return total_string
        print(total_string)
    if politician == "bloomberg":
        total_string=""
        for tweet in bloomberg:
            total_string += str(tweet)
        return total_string
        print(total_string)
    if politician == "buttigieg":
        total_string=""
        for tweet in buttigieg:
            total_string += str(tweet)
        return total_string
        print(total_string)
    if politician == "de_la_fuente":
        total_string=""
        for tweet in de_la_fuente:
            total_string += str(tweet)
        return total_string
        print(total_string)
    if politician == "gabbard":
        total_string=""
        for tweet in gabbard:
            total_string += str(tweet)
        return total_string
        print(total_string)
    if politician == "klobuchar":
        total_string=""
        for tweet in klobuchar:
            total_string += str(tweet)
        return total_string
        print(total_string)
    if politician == "sanders":
        total_string=""
        for tweet in sanders:
            total_string += str(tweet)
        return total_string
        print(total_string)
    if politician == "trump":
        total_string=""
        for tweet in trump:
            total_string += str(tweet)
        return total_string
        print(total_string)
    if politician == "warren":
        total_string=""
        for tweet in warren:
            total_string += str(tweet)
        return total_string
        print(total_string)



analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(text):
    if text is not None:
        score = analyzer.polarity_scores(text)
        return[score, text]
    else:
        pass

def snip_full_text_to_word(full_text, word):
    if word not in full_text:
        print("")
    else:
        start_of_word = full_text.find(word)
        if start_of_word >= 100:
            start_bound = start_of_word - 100
        elif start_of_word < 100:
            start_bound = 0
        if (start_of_word + 100) <= len(full_text):
            end_bound = start_of_word + 100
        elif (start_of_word + 100) > len(full_text):
            end_bound = len(full_text)
        text = full_text[start_bound:end_bound]
        return text

def get_politician_sentiment(politician, issue):
    newwords=[]
    input_file = open("issues/" + issue + ".txt", "r")
    words = input_file.read()
    input_file.close()


    # calculate the average sentiment value (sum / length)
    neg_val = (sum([sentiment_analyzer_scores(snip_full_text_to_word(get_politician_tweets(politician), word))[0]['neg'] for word in words]))/len(words)
    neu_val = (sum([sentiment_analyzer_scores(snip_full_text_to_word(get_politician_tweets(politician), word))[0]['neu'] for word in words]))/len(words)
    pos_val = (sum([sentiment_analyzer_scores(snip_full_text_to_word(get_politician_tweets(politician), word))[0]['pos'] for word in words]))/len(words)
    compound_val = (sum([sentiment_analyzer_scores(snip_full_text_to_word(get_politician_tweets(politician), word))[0]['compound'] for word in words]))/len(words)
    return [neg_val, neu_val, pos_val, compound_val, ""] # replaced quotation with empty string


@app.route('/')
def index():
    return render_template('index.html')

def net_sentiment(pos,neg):
    return (pos-neg)





@app.route('/biden')
def _biden():
    politician="biden"
    mypolitician = "Joe Biden"
    sentiment_values = {
        "abortion": [0.05490909090909091,0.22536363636363638],
        "immigration": [0.24255851063829745, 0.007776595744680851],
        "weapons": [0.2338175675675675, 0.01942905405405408],
        "education": [0.19822448979591836, 0.04565306122448979],
        "terrorism": [0.20431034482758617, 0.04103448275862069],
        "foreign": [0.2094931506849315, 0.0374931506849315],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)
@app.route('/bloomberg')
def _bloomberg():
    politician="bloomberg"
    mypolitician = "Mike Bloomberg"
    sentiment_values = {
        "abortion": [0.020363636363636365, 0.1958181818181818],
        "immigration": [0.020319148936170203, 0.1727127659574467],
        "weapons": [0.016638513513513496, 0.1821655405405391],
        "education": [0.018061224489795923, 0.17114285714285712],
        "terrorism": [0.02767241379310344, 0.17206896551724132],
        "foreign": [0.01665753424657534, 0.17665753424657532],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)
@app.route('/sanders')
def _sanders():
    politician="sanders"
    mypolitician = "Bernie Sanders"
    sentiment_values = {
        "abortion": [0.12527272727272726, 0.05454545454545454],
        "immigration": [0.10477127659574477,0.029340425531914894],
        "weapons": [0.10999825783972081, 0.02996167247386758],
        "education": [0.11991836734693878, 0.0326530612244898],
        "terrorism": [0.11149999999999997, 0.051189655172413785],
        "foreign": [0.11497260273972601, 0.03904109589041095],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)
@app.route('/buttigieg')
def _buttigieg():
    politician="buttigieg"
    mypolitician = "Pete Buttigieg"
    sentiment_values = {
        "abortion": [0.25099999999999995, 0.012636363636363638],
        "immigration": [0.25710106382978776, 0.009117021276595746],
        "weapons": [0.24908783783783814, 0.010689189189189196],
        "education": [0.21583673469387757, 0.01979591836734694],
        "terrorism": [0.19991379310344828, 0.030896551724137935],
        "foreign": [0.22405479452054802, 0.01904109589041096],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)
@app.route('/de_la_fuente')
def _de_la_fuente():
    politician="de_la_fuente"
    mypolitician = "Roque De La Fuente"
    sentiment_values = {
        "abortion": [0.2502727272727273, 0.059454545454545454],
        "immigration": [0.2557393617021279, 0.06480319148936163],
        "weapons": [0.2463496621621625, 0.07145777027027049],
        "education": [0.22332653061224492, 0.06391836734693877],
        "terrorism": [0.2313793103448276, 0.060137931034482756],
        "foreign": [0.22320547945205485, 0.0654383561643836],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)
@app.route('/gabbard')
def _gabbard():
    politician="gabbard"
    mypolitician = "Tulsi Gabbard"
    sentiment_values = {
        "abortion": [0.010363636363636365, 0.0],
        "immigration": [0.006893617021276597, 0.006664893617021277],
        "weapons": [0.009006756756756756, 0.010694256756756759],
        "education": [0.021897959183673467, 0.0039387755102040815],
        "terrorism": [0.032965517241379326, 0.012999999999999998],
        "foreign": [0.026315068493150694, 0.009287671232876712],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)
@app.route('/klobuchar')
def _klobuchar():
    politician="klobuchar"
    mypolitician = "Amy Klobuchar"
    sentiment_values = {
        "abortion": [0.1989090909090909, 0.033545454545454545],
        "immigration": [0.20280851063829802, 0.010648936170212769],
        "weapons": [0.19474493243243196, 0.016601351351351375],
        "education": [0.1843469387755102, 0.026551020408163265],
        "terrorism": [0.19094827586206894, 0.02246551724137931],
        "foreign": [0.19760273972602735, 0.025356164383561645],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)
@app.route('/trump')
def _trump():
    politician="trump"
    mypolitician = "Donald Trump"
    sentiment_values = {
        "abortion": [0.19772727272727272, 0.11390909090909095],
        "immigration": [0.17782446808510627, 0.09922872340425529],
        "weapons": [0.18383783783783772, 0.10909290540540587],
        "education": [0.18363265306122456, 0.10402040816326533],
        "terrorism": [0.16068965517241382, 0.10513793103448277],
        "foreign": [0.160068493150685, 0.09824657534246578],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)
@app.route('/warren')
def _warren():
    politician="warren"
    mypolitician = "Elizabeth Warren"
    sentiment_values = {
        "abortion": [0.11318181818181818, 0.004727272727272727],
        "immigration": [0.10190425531914901, 0.01520744680851064],
        "weapons": [0.11033277027027037, 0.0086875],
        "education": [0.10212244897959181, 0.011734693877551019],
        "terrorism": [0.09391379310344829, 0.015689655172413792],
        "foreign": [0.09923287671232878, 0.007520547945205479],
    }
    return render_template("politician_overview.html",sentiment_values=sentiment_values, mypolitician=mypolitician,politician=politician)







@app.route('/<politician>/<issue>')
def politician_sentiment_on_issue(politician, issue):
    neg_val = get_politician_sentiment(politician, issue)[0]
    neu_val = get_politician_sentiment(politician, issue)[1]
    pos_val = get_politician_sentiment(politician, issue)[2]
    compound_val = get_politician_sentiment(politician, issue)[3]
    quotation = "..." + str(get_politician_sentiment(politician, issue)[4]) + "..."
    quotation1 = quotation[0:quotation.find(str(issue))]
    quotation2 = quotation[quotation.find(str(issue)):(quotation.find(str(issue))+len(issue))]
    mypolitician = politician.capitalize()
    myissue = issue.capitalize()
    if politician == "biden": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/JoeBiden?ref_src=twsrc%5Etfw">Tweets by JoeBiden</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if politician == "bloomberg": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/MikeBloomberg?ref_src=twsrc%5Etfw">Tweets by MikeBloomberg</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if politician == "buttigieg": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/PeteButtigieg?ref_src=twsrc%5Etfw">Tweets by PeteButtigieg</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if politician == "de_la_fuente": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/JoinRocky?ref_src=twsrc%5Etfw">Tweets by JoinRocky</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if politician == "gabbard": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/TulsiGabbard?ref_src=twsrc%5Etfw">Tweets by TulsiGabbard</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if politician == "klobuchar": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/amyklobuchar?ref_src=twsrc%5Etfw">Tweets by amyklobuchar</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if politician == "sanders": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/BernieSanders?ref_src=twsrc%5Etfw">Tweets by BernieSanders</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if politician == "trump": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/realDonaldTrump?ref_src=twsrc%5Etfw">Tweets by realDonaldTrump</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if politician == "warren": ttweet = '<a class="twitter-timeline" data-width="300" data-height="300" href="https://twitter.com/ewarren?ref_src=twsrc%5Etfw">Tweets by ewarren</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
    if mypolitician == "De_la_fuente": mypolitician = "De La Fuente"
    return render_template(
        "template.html",
        x_vals = ["Negative", "Neutral", "Positive", "Compound"],
        y_vals = [neg_val, neu_val,pos_val,compound_val],
        quotation=quotation,
        quotation1 = quotation1,
        issue = issue,
        quotation2 = quotation2,
        imglinks = ["https://twitframe.com/show?url=https://twitter.com/MikeBloomberg/status/1233228979735351297","https://twitframe.com/show?url=https://twitter.com/MikeBloomberg/status/1233165752447963137", "https://twitframe.com/show?url=https://twitter.com/maggielea31/status/1233169132809416704"],
        mypolitician=mypolitician,
        myissue=myissue,
        ttweet=ttweet,
        politician = politician,
    )

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
