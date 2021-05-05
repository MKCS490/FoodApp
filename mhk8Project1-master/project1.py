import flask
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import os
import random
from os.path import join, dirname
from dotenv import load_dotenv
import json
import requests

app = flask.Flask(__name__)

dotenv_pathTweepy = join(dirname(__file__), 'tweepy.env')
load_dotenv(dotenv_pathTweepy)

dotenv_pathSpoon = join(dirname(__file__), 'spoonacular.env')
load_dotenv(dotenv_pathSpoon)

spoonacular_key = os.environ['SPOONACULAR_KEY']

consumer_key=os.environ["oauth_consumer_key"]
consumer_secret=os.environ["oauth_consumer_secret"]
access_token=os.environ["oauth_token"]
access_token_secret=os.environ["oauth_token_secret"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

@app.route('/')
def index():
    foods = ['Caesar Salad', 'Chana Masala', 'Keema Naan', 
    'Fajitas', 'Chicken Rice', 'Dumplings']

    currentFood = random.choice(foods)
    releventTweet=[]
    userName=[]
    tweetTime = []
    
    if currentFood == "Caesar Salad":
        url = ("https://api.spoonacular.com/recipes/extract?url=https://natashaskitchen.com/caesar-salad-recipe/&apiKey={}").format(spoonacular_key)
    
    elif currentFood == "Chana Masala":
        url = ("https://api.spoonacular.com/recipes/extract?url=https://minimalistbaker.com/easy-chana-masala//&apiKey={}").format(spoonacular_key)
    
    elif currentFood == "Keema Naan":
        url = ("https://api.spoonacular.com/recipes/extract?url=https://fatimacooks.net/easy-keema-naan-recipe-in-the-oven-tawa/&apiKey={}").format(spoonacular_key)
    
    elif currentFood == "Fajitas":
        url = ("https://api.spoonacular.com/recipes/extract?url=https://www.spendwithpennies.com/easy-chicken-fajitas/&apiKey={}").format(spoonacular_key)
    
    elif currentFood == "Chicken Rice":
        url = ("https://api.spoonacular.com/recipes/extract?url=https://dinnerthendessert.com/halal-carts-middle-eastern-chicken-and-rice/&apiKey={}").format(spoonacular_key)
    
    elif currentFood == "Dumplings":
        url = ("https://api.spoonacular.com/recipes/extract?url=https://www.tasteofhome.com/recipes/the-best-chicken-dumplings/&apiKey={}").format(spoonacular_key)
    
    
    response = requests.get(url)
    json_body = response.json()
    
    instructions = json.loads(json.dumps(json_body["instructions"]))

    rawIngredients = json.loads(json.dumps(json_body['extendedIngredients']))
    
    image = json.loads(json.dumps(json_body["image"]))
    
    sourceUrl = json.loads(json.dumps(json_body['sourceUrl']))
    
    servings = json.loads(json.dumps(json_body["servings"]))

    i = 0
    ingredients = ""
    for value in rawIngredients:
        ingredients += (rawIngredients[i]['name'] + ", \n")
        i += 1
    
    
    for tweet in Cursor(auth_api.search,q= currentFood,
                    lang='en',
                    tweet_mode="extended").items():
        releventTweet = (tweet.full_text)
        userName = (tweet.user.screen_name)
        tweetTime=(tweet.created_at)
        break
    at = '@'
    userName = at + userName
    
    return flask.render_template(
        "tweets.html",
        current_Food= currentFood,
        relevent_Tweet= releventTweet,
        user_Name= userName,
        tweet_time = tweetTime,
        recipe_Instructions = instructions,
        recipe_Ingredients = ingredients,
        recipe_Image = image,
        source_URL = sourceUrl,
        serving_Size = servings)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    )