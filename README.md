
# 🧠 Quiz Website

A simple yet interactive quiz platform developed using **Flask**. The application allows users to answer multiple-choice questions, view their scores, and enjoy a clean and modern UI.

---

## 📜 Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How to Run Locally](#-how-to-run-locally)
- [License](#license)

---

## ✨ Features
- User-friendly interface.
- Displays multiple-choice questions.
- Tracks user scores and displays results.
- Fully responsive design for desktop and mobile devices.
- Easy to customize and extend with additional questions or features.

---

## 📸 Screenshots

### Home Page
![Home Page](https://github.com/ShrihariKasar/Quiz-Website/blob/main/Screenshots/Start.png)

### Quiz Page
![Quiz Page](https://github.com/ShrihariKasar/Quiz-Website/blob/main/Screenshots/Quiz.png)

### Result Page
![Result Page](https://github.com/ShrihariKasar/Quiz-Website/blob/main/Screenshots/Result.png)

---

## 🛠️ Technologies Used
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Flask (Python)
- **Styling**: Custom CSS
- **Data Storage**: JSON

---

## 📂 Project Structure

```plaintext
quiz-website/
│
├── static/                # Contains static files
│   └── style.css          # CSS for styling
│
├── templates/             # Contains HTML templates
│   ├── home.html          # Home page
│   ├── quiz.html          # Quiz page
│   └── result.html        # Result page
│
├── app.py                 # Main Flask application
├── questions.json         # JSON file with quiz questions
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🚀 How to Run Locally

Follow these steps to run the project on your local machine:

### Prerequisites:
- Python 3.x installed
- A code editor (e.g., VSCode) and a browser
- Git for version control (optional)

### Steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShrihariKasar/quiz-website.git
   cd quiz-website
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/macOS
   venv\Scripts\activate      # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App**:
   ```bash
   python app.py
   ```

5. **Open the Application**:
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to fork the repository, raise issues, and contribute to enhance this project. Enjoy building your quiz website! 😊
```
Let me know if you need further edits! 🚀
