#!/usr/bin/python3

import csv
import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_json():
    with open(os.path.join(BASE_DIR, "products.json"), "r") as file:
        return json.load(file)


def read_csv():
    products = []
    with open(os.path.join(BASE_DIR, "products.csv"), "r", newline="") as file:
        for row in csv.DictReader(file):
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():
    items_list = []
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
        items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template("items.html", items=items_list)


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Choose the data source
    try:
        if source == "json":
            data = read_json()
        elif source == "csv":
            data = read_csv()
        else:
            return render_template("product_display.html", error="Wrong source")
    except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
        return render_template("product_display.html", error="Could not read data file")

    # Filter by id if provided
    if product_id is not None:
        try:
            wanted = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Product not found")
        data = [p for p in data if p.get("id") == wanted]
        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
