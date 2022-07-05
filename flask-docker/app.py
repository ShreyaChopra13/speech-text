from django.shortcuts import render
from flask import Flask, render_template
import model as p

app = Flask(__name__)

@app.route('/')
def sr():

  return p.srmodel()


if __name__ == '__main__':
  app.run(debug=True)


