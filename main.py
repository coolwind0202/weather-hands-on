from flask import Flask, render_template
import requests

app = Flask(__name__)
url = "https://weather.tsukumijima.net/api/forecast/city/016010"


@app.route("/")
def hello_world():
    raw_forecast = requests.get(url).json()

    def convert_forecast(forecast):
        _, m, d = forecast["date"].split("-")
        forecast["date"] = f"{m}月{d}日"

        temp_min = forecast["temperature"]["min"]["celsius"]
        temp_max = forecast["temperature"]["max"]["celsius"]

        forecast["temperature"]["min"] = temp_min if temp_min is not None else "なし"
        forecast["temperature"]["max"] = temp_max if temp_max is not None else "なし"

        return forecast

    raw_forecast["forecasts"] = map(
        convert_forecast, raw_forecast["forecasts"])

    return render_template("index.html", data=raw_forecast)
