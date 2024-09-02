# AI-Powered News Summarizer

### Overview

The AI-Powered News Summarizer is a Python-based application designed to fetch, summarize, and analyze the sentiment of news articles. Using `newspaper3k` for web scraping and `TextBlob` for sentiment analysis, this tool allows users to quickly grasp the essence of news articles by providing concise summaries and sentiment insights.

### Features

- URL Input: Users can input the URL of any news article.
- Automatic Summarization: The app extracts the title, author(s), publication date, and a summary of the article.
- Sentiment Analysis: Provides sentiment polarity (positive, negative, neutral) based on the article's content.
- User-Friendly Interface: Simple and clean UI built with Tkinter.

### Screenshots

![image](https://github.com/user-attachments/assets/144400ab-3fe4-4a0c-851b-7f72b1dd522f)


### Installation

1. Clone the Repository:

   ```bash
   git clone https://github.com/Adeel-Farooq-Khan/News-Summarizer.git
   cd news-summarizer
   ```

2. Create a Virtual Environment (Optional but Recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```


3. Install the Required Libraries:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Application:

   ```bash
   python main.py
   ```
### Requirements

- Python 3.12.4
- Tkinter (Usually included with Python)
- newspaper3k
- TextBlob

### Usage

1. Enter the News Article URL:
   - Paste the URL of the news article you wish to summarize in the input field at the top.

2. Click on 'Summarize':
   - The application will fetch the article, generate a summary, and perform sentiment analysis.

3. View the Results:
   - The title, author(s), publication date, summary, and sentiment analysis will be displayed in the respective fields.


### Contributing

Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request with your changes.


### Contact

For any questions or issues, please feel free to reach out:

- Email: [your-email@example.com](mailto:adeelfarooq417@gmail.com)
- GitHub: [your-username](https://github.com/Adeel-Farooq-Khan)
- LinkedIn: [Your Name](https://linkedin.com/in/adeel-farooq-khan)
