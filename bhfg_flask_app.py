"""
Title: Black History Facts Generator
Creator: Brittany Gates (https://github.com/bcgates82/ | https://twitter.com/bgates_writer)
About: In celebration of Black History Month I've created a random Black History Facts generator.
Fact Sources:
http://www.history.com/topics/black-history/black-history-facts
http://www.history.com/topics/black-history/black-history-milestones
http://www.history.com/topics/black-history/booker-t-washington
http://www.history.com/topics/black-history/george-washington-carver
https://en.wikipedia.org/wiki/W._E._B._Du_Bois
"""

from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    This function opens and reads the bhfg_facts.txt file which is located in the Static (/static/) directory.
    Then a loop runs over the entire file, reading each line. The loop collects all the lines as a list, and then
    pulls out one fact randomly using the random.choice function.

    :return: The function returns a random Black History Fact to the home.html template, which displays it on the
    website.
    """

    with open('static/files/bhfg_facts.txt', 'r') as facts:
        fact_list = facts.readlines()
    return render_template('index.html', black_history_fact=random.choice(fact_list))
