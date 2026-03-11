# 🏋️ Workout Tracker

A Python app that uses **Natural Language Processing** to log your workouts automatically into a Google Sheet via the **Nutritionix API** and **Sheety API**.

Simply type what exercise you did (e.g. *"I ran 5km and did 30 minutes of cycling"*), and the app will extract the exercise details and log them with date, time, duration, and calories burned.

---

## ⚠️ Note on API Availability

> This project currently may **not run as expected** due to policy changes in the **Nutritionix** and/or **Sheety** APIs. Free-tier access and certain endpoints may be restricted or require upgraded plans. Please check the latest documentation for both services before running.

---

## 🚀 Features

- Natural language exercise input
- Automatic calorie and duration extraction via Nutritionix
- Logs workout data to Google Sheets via Sheety
- Records date and time of each workout automatically

---

## 🛠️ Tech Stack

- Python 3
- Nutritionix API
- Sheety API
- Google Sheets

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/workout-tracker.git
   cd workout-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory with the following variables:

   ```
   NUTRITIONIX_APP_ID=your_nutritionix_app_id
   NUTRITIONIX_API_KEY=your_nutritionix_api_key
   SHEET_ENDPOINT=your_sheety_endpoint_url
   USER_PASS=Bearer your_sheety_token
   ```

---

## ▶️ Usage

```bash
python main.py
```

When prompted, type your exercise in plain English:

```
What exercise did you do? I did 30 minutes of running and 20 minutes of cycling
```

The app will log it to your Google Sheet automatically.

---

## 📊 Google Sheet Columns

| Date | Time | Exercise | Duration (min) | Calories |
|------|------|----------|----------------|----------|

---

## 🔑 API Setup

### Nutritionix
- Sign up at [nutritionix.com](https://www.nutritionix.com/business/api)
- Get your `App ID` and `API Key`

### Sheety
- Sign up at [sheety.co](https://sheety.co)
- Create a Google Sheet and connect it via Sheety
- Enable `POST` requests and set up **Bearer Token** authentication

---

## 📄 License

This project is for educational purposes.
