import subprocess
from pathlib import Path
import os
import openai
import dotenv
import nltk
import md2pdf
from PyPDF2 import PdfReader
import deepl
import argparse
from md2pdf.core import md2pdf

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from PIL import Image


def load_text(path):
    with open(path, "r") as f:
        return f.read()


def save_text(text, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def summarize_text(text, summary_ratio=0.2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(
        parser.document, summary_ratio * len(list(parser.document.sentences))
    )
    return " ".join([str(sentence) for sentence in summary])


def extract_images(pdf_path, output_path):
    output_path.mkdir(parents=True, exist_ok=True)
    p = subprocess.run(
        f"python -m fitz extract -images {pdf_path} -output {output_path}",
        shell=True,
        capture_output=True,
    )

    print(p.stdout.decode("utf-8"))
    print(p.stderr.decode("utf-8"))

    # make a list containing all the image paths
    images = []
    for file in output_path.iterdir():
        if file.suffix == ".png":
            # resize the image to 600px wide
            image = Image.open(file)
            width, height = image.size
            new_width = 600
            new_height = height * (new_width / width)
            image = image.resize((new_width, int(new_height)))
            image.save(file)

            images.append(file)

    return images


def extract_text(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    all_text = ""
    for page in reader.pages:
        all_text += page.extract_text()

    all_text = " ".join(nltk.tokenize.word_tokenize(all_text))
    all_text = " ".join(nltk.tokenize.wordpunct_tokenize(all_text))

    return all_text


def summarize_with_gpt(text):
    _prompt = load_text("prompts/summarize_text.txt")
    prompt = "PAPER STARTS HERE\n" + text + _prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        top_p=1.0,
        n=1,
        best_of=2,
    )

    summary = response.choices[0].text

    if response.choices[0].finish_reason == "stop":
        print("GPT-3 finished because it reached the stop token.")
    else:
        print("GPT-3 finished because it reached the max tokens.")
        print(response.choices[0].finish_reason)
    return summary


def translate_text(text, target_lang="JA"):
    return translator.translate_text(text, target_lang=target_lang).text


def make_markdown_file(summary, summary_ja, images, output_path):
    with open(output_path / "summary.md", "w") as f:
        f.write("## Summary\n")
        f.write(summary)
        f.write("\n\n")
        f.write("## Summary (Japanese)\n")
        f.write(summary_ja)
        f.write("\n\n")
        f.write("## Images\n")
        for image in images:
            f.write(f"![{image.stem}]({image})\n\n")


def convert_markdown_to_pdf(input_path, output_path):
    # poetry run md2pdf /Users/atom/Github/gpt_arxiv_summary/2101.05388/summary.md output.pdf
    p = subprocess.run(
        f"md2pdf {input_path} {output_path}",
        shell=True,
        capture_output=True,
    )

    print(p.stdout.decode("utf-8"))
    print(p.stderr.decode("utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pdf_path", help="path to input pdf file")
    parser.add_argument(
        "-o", "--out_path", help="path to output file", default=Path(".")
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    output = Path(args.out_path) / pdf_path.stem

    dotenv.load_dotenv()
    nltk.download("punkt")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

    images = extract_images(pdf_path, output)
    text = extract_text(pdf_path, output)

    smaller_text = summarize_text(text, summary_ratio=0.1)
    summary = summarize_with_gpt(smaller_text)
    summary_ja = translate_text(summary, target_lang="JA")

    save_text(text, output / "text.txt")
    save_text(summary, output / "summary.txt")
    save_text(summary_ja, output / "summary_ja.txt")

    make_markdown_file(summary, summary_ja, images, output)
    convert_markdown_to_pdf(output / "summary.md", output / "summary.pdf")
