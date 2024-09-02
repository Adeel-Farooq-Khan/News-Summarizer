import tkinter as tk
from textblob import TextBlob
from newspaper import Article

def summarize():
    url = utext.get('1.0', 'end').strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', ', '.join(article.authors))

    publication.delete('1.0', 'end')
    publication.insert('1.0', str(article.publish_date))

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f"Polarity: {analysis.polarity} | Sentiment: {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}")

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

root = tk.Tk()
root.title("News Summarizer")
root.geometry("800x600")
root.configure(bg='#f2f2f2')

url_frame = tk.Frame(root, bg='#f2f2f2')
url_frame.pack(pady=10)
ulabel = tk.Label(url_frame, text="Enter URL:", font=("Helvetica", 12), bg='#f2f2f2')
ulabel.pack(side=tk.LEFT)
utext = tk.Text(url_frame, height=1, width=100, font=("Helvetica", 12), bd=2)
utext.pack(side=tk.LEFT)

tlabel = tk.Label(root, text="Title", font=("Helvetica", 12), bg='#f2f2f2')
tlabel.pack(pady=5)
title = tk.Text(root, height=1, width=100, font=("Helvetica", 12), bd=2)
title.config(state='disabled', bg='#ffffff')
title.pack()

alabel = tk.Label(root, text="Author(s)", font=("Helvetica", 12), bg='#f2f2f2')
alabel.pack(pady=5)
author = tk.Text(root, height=1, width=100, font=("Helvetica", 12), bd=2)
author.config(state='disabled', bg='#ffffff')
author.pack()

plabel = tk.Label(root, text="Publishing Date", font=("Helvetica", 12), bg='#f2f2f2')
plabel.pack(pady=5)
publication = tk.Text(root, height=1, width=100, font=("Helvetica", 12), bd=2)
publication.config(state='disabled', bg='#ffffff')
publication.pack()

xlabel = tk.Label(root, text="Summary", font=("Helvetica", 12), bg='#f2f2f2')
xlabel.pack(pady=5)
summary = tk.Text(root, height=10, width=100, font=("Helvetica", 12), bd=2)
summary.config(state='disabled', bg='#ffffff')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis", font=("Helvetica", 12), bg='#f2f2f2')
selabel.pack(pady=5)
sentiment = tk.Text(root, height=1, width=100, font=("Helvetica", 12), bd=2)
sentiment.config(state='disabled', bg='#ffffff')
sentiment.pack()

btn = tk.Button(root, text="Summarize", font=("Helvetica", 12), command=summarize, bg='#4CAF50', fg='#ffffff', bd=2)
btn.pack(pady=20)

root.mainloop()
