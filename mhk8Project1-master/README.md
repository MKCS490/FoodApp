To use this repository, you must follow these steps:
0. Sign up for a twitter developer account
  https://developer.twitter.com/en/apply-for-access
1. make a new app on https://developer.twitter.com/en/portal/projects-and-apps
2. Acess your token keys which you will use in your code
2.5 Sign up for spoonacular at https://spoonacular.com/food-api/console.
2.6 Navigate to https://spoonacular.com/food-api/console#Profile and find your API Key (THIS IS SECRET, DO NOT SHOW THIS TO OTHERS!).
3. To use the tweepy API run the following command in your terminal
  sudo pip3 install tweepy
4. Install flask sudo pipe3 install flask
5. Install python dotenv sudo pipe3 install python-dotenv
5.5 import requests
6. create a tweepy.env file
  you are doing this so you dont put your secret keys in your python file for the whole world to see.
  paste the following in your .env file and fill in with secret keys.
   KEY=''
   KEY_SECRET=''
   TOKEN=''
   TOKEN_SECRET=''
6.5 create a new root-level file called spoonacular.env
6.6 Add the following line in spoonacular.env: 
    SPOONACULAR_KEY='your_key_here'
6.7 Run the following, where the brackets indicate optional changes to the command you may have to run:
    [sudo] [/path/to/]pip[3] install python-dotenv
6.8 Save spoonacular.env and run your python file.
7. In your python file you will import os and will set the env variables to os.environ["oauth_consumer_key"]
  ex consumer_key=os.environ["oauth_consumer_key"]
8. import flask in your python file. Flask will help us build the web application.
  to initialize flask
  @app.route('/')
  def index():
  **put code here**
  
   in the return statement pass the html file, and all the variables you will be using in the html file.
   example
   return flask.render_template(
        "tweets.html",
        current_Food= currentFood)
 
 9. For the actual code I declared a foods variable as a list.
 10. import random. I used random to pick a random food to display on the page. I then set the random food to the variable currentFood.
 11. I created a list variable for releventTweet,userName, tweetTime
 12. I used a for loop and used the tweepy search API. I set q = currentFood, lanugage is set to english, and the tweet length is set to extended so the whole tweet is shown
 then the data I gather from search I store it in the correct variables. For example releventTweet would be (tweet.full_text) I broke out of the loop after 1 iteration because
 we only want to display 1 tweet. 
 12.2 To extract certain recipe from a website I used the following link:
      "https://api.spoonacular.com/recipes/extract?url=YOURURL&apiKey={}"
 12.5 Once I had the URl I did 
 response = requests.get(url)
 json_body = response.json() 
 12.6 Now if I wanted to get the instructions I would type the following:
      instructions = json.loads(json.dumps(json_body["instructions"]))
      same process to get ingreditents, url, serving size, and the picture url
 13. At the end of the program we want to run the web app. We do so with the following command
 app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
    )
 14. Now we open to the HTML file in the template folder, tweets.html
 15. In the header we link the style.css
 16. In the body we display the variables which we passed the render template
  we have to use a certain syntax for that for example:
  h1 {{ current_Food }} h1
  17. I named h1, h2, h3, and h4 that made it easier in my css
  18. Now we make and open the style.css file in the static folder.
  19. go back and link the style.css path in html header
  20. I went to google fonts and imported a font from there called 'Fredoka One'
  21. I downloaded a background from the internet by using the wget command in my static folder. 
  22. I imported that background in my body section. Also made it appear only once.
  23. I edited my h1, h2,h3,h4 tags and adding certain padding values to make them appear where I wanted them to appear.
  24. Sign up for heroku at heroku.com 
  25. Install heroku by running npm install -g heroku
  26. Go through the following steps:
      heroku login -i
      heroku create
  27. Navigate to your newly-created heroku site!
  28. Add your secret keys (from tweepy.env) by going to https://dashboard.heroku.com/apps
      and clicking into your app. Click on Settings, then scroll to "Config Vars." Click
      "Reveal Config Vars" and add the key value pairs for each variable in user_tweets.py
      Your config var key names should be:
      SPOONACULAR_KEY
      oauth_token_secret
      oauth_token
      oauth_consumer_secret
      oauth_consumer_key
   29. Configure requirements.txt with all requirements needed to run your app.
   30. Configure Procfile with the command needed to run your app.
   31. commit and push your code to github
   32. run $ git push heroku master
   33. Visit your new and running app
  
   34. TECHNICAL ISSUE
      1- I was having trouble displaying the variables in HTML that was because I was passing the wrong variables and had syntax error.
      2- In my style.css I had trouble displaying the text in the middle of the screen. I solved that by looking at different types on padding and sizes, widths.
      3. I had trouble displaying the background on different screens. On my laptop it would show up full screen, but on my monitor it was not covering the screen. I solved this           by setting background size to cover. 
      4. I had trouble printing the instructions data. I found out that it was raw data and all the \n \t characters were showing. I used json.loads(json.dumps()) and that                 solved the issue.
   35. KNOWN ISSUE
      1- I have an issue with displaying tweets. Sometimes the some of the text of the tweet shows as ...." If I have more time I would look at the tweepy search and figure 
      out what is the issue.
      2- Another issue I have is that sometimes if you press refresh really fast it would show the same tweet. Next time I would create an array with the saved tweets. Then 
      I would make a loop and dislay a random tweet everytime.
