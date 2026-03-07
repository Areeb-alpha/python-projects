# 📊 Pixela Habit Tracker

A Python script to track daily habits using the [Pixela](https://pixe.la/) API. Visualizes your progress as a GitHub-style heatmap graph.

---

## 🚀 Features

- Create a Pixela user account
- Create a custom habit tracking graph
- Log daily habit data (e.g. weight, steps, calories)
- Update or delete existing entries

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/habit-tracker.git
cd habit-tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Create a `.env` file in the root directory with the following:

```env
TOKEN=your_secret_token
PIXELA_USERNAME=your_pixela_username
GRAPH_ID=your_graph_id
```

> ⚠️ Never share or commit your `.env` file. Add it to `.gitignore`.

### 4. First-time setup

On the **first run only**, uncomment these lines in `main.py` to create your user and graph:

```python
response = requests.post(url=PIXELA_API, json=PIXELA_PARAMETERS)
response = requests.post(url=graph_api, json=graph_params, headers=HEADERS)
```

After running once, **comment them out again** to avoid errors on future runs.

---

## ▶️ Usage

```bash
python main.py
```

You will be prompted to enter today's value:

```
How many kg or grams have you burned today?: 0.5
```

---

## 📈 View Your Graph

Open this URL in your browser:

```
https://pixe.la/v1/users/YOUR_USERNAME/graphs/YOUR_GRAPH_ID.html
```

Replace `YOUR_USERNAME` and `YOUR_GRAPH_ID` with your actual values.

---

## ✏️ Update a Pixel

To update an existing entry, uncomment this section in `main.py`:

```python
post_params = {"quantity": "59"}
response = requests.put(url=put_api, json=post_params, headers=HEADERS)
print(response.text)
```

---

## 🗑️ Delete a Pixel

To delete an existing entry, uncomment this section in `main.py`:

```python
response = requests.delete(url=delete_pixel_api, headers=HEADERS)
print(response.text)
```

---

## 📁 Project Structure

```
habit-tracker/
│
├── main.py           # Main script
├── .env              # Environment variables (not committed)
├── .gitignore        # Ignores .env and other files
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## 📝 Notes

- Pixela's free tier randomly rejects ~25% of requests. Simply re-run if this happens.
- The `print(786)` at the top is a personal touch — feel free to remove it!

---

## 📄 License

MIT License
