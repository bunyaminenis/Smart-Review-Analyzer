# 🧠 Smart Review Analyzer Dashboard

A Streamlit-based AI dashboard for analyzing customer reviews using sentiment analysis. Upload a CSV file of reviews, automatically classify them as positive, negative, or neutral, and visualize the results with interactive charts and filters.

---

## 🚀 Features

- 📤 Upload your own review CSV file
- 🤖 Sentiment analysis using TextBlob
- 📊 Pie or bar chart showing sentiment distribution
- 🔍 Filter reviews by sentiment (positive, negative, neutral)
- 📥 Download filtered results as CSV
- 🧪 Load example dataset for testing
- 🎨 Clean layout using Streamlit sidebar and column layout

---

## 📦 Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
- [Matplotlib](https://matplotlib.org/)

---

## 🧰 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bunyaminenis/Smart-Review-Analyzer.git
cd smart-review-analyzer

Install Dependencies
pip install -r requirements.txt
Run the App
streamlit run smart_review_analyzer.py

📄 File Format
Make sure your CSV file includes a column named review_text. Example:
| review\_id | review\_text                        |
| ---------- | ----------------------------------- |
| 101        | This product is amazing! I love it. |
| 102        | Terrible experience. Never again.   |

📤 Output
You can download filtered reviews in CSV format after applying sentiment filters.

✅ To Do (Optional Enhancements)
Use HuggingFace Transformers for advanced sentiment detection

Add product category filters

Export results as PDF

Deploy to Streamlit Cloud or HuggingFace Spaces

🧑‍💻 Author
Your Name – @bunyaminenis

📃 License
This project is licensed under the MIT License.
