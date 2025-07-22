# 📝 AI Blog Writer (GPT-Neo 1.3B)
Generate detailed blog posts (8–10+ paragraphs) with an open-source LLM , Create long-form, detailed blog posts instantly using the open-source GPT-Neo 1.3B model — completely free and offline.

This project provides a simple and powerful blog writing assistant built with **Streamlit** and **Hugging Face Transformers**. It uses the **GPT-Neo 1.3B** language model from EleutherAI to generate high-quality blog posts of 5–10 paragraphs based on any topic you enter.

Unlike commercial AI tools, this app requires **no API keys**, runs **entirely offline**, and is ideal for writers, students, researchers, and anyone interested in experimenting with large language models locally.


---

## 🚀 Features

- ✅ Generates detailed 5–10 paragraph blog posts
- ✅ Runs fully offline (no API required)
- ✅ Uses open-source GPT-Neo 1.3B from Hugging Face
- ✅ Streamlit-based web interface
- ✅ Deterministic output with `set_seed()`
- ✅ Lightweight and easy to use

---

## 🛠️ Requirements

○ Python 3.8+

○ At least 6 GB RAM (8 GB recommended)

○ Internet (only once to download model weights)

---

## 📦 Installation

  1. Clone the repository

```bash
git clone https://github.com/yourusername/gptneo-blog-writer.git
cd gptneo-blog-writer
```
  2. Create and activate virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate         # On Windows
# or
source venv/bin/activate      # On macOS/Linux
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---


▶️ Usage

```bash
streamlit run app.py
```
Then open your browser at:
http://localhost:8501


---

📂 Project Structure

```bash
gptneo-blog-writer/
├── genai_blog_writer.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

📌 Notes

  •  GPT-Neo 1.3B is a large model. Running locally requires ~6 GB of RAM.

 • If you experience performance issues, try smaller models like gpt2-large


---


🙋‍♂️ Credits

 • EleutherAI for GPT-Neo 1.3B

 • Hugging Face Transformers

 • Streamlit


---


📄 License

 •  This project is licensed under the MIT License.






