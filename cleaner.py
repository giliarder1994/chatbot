import re

def remove_chat_metadata(chat_export_file):
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  #ex: "1/15/26, 14:50"
    dash_whitespace = r"\s-\s"   # " - "
    username = r"([\w\s]+)"   # ex: "Martin"
    metadata_end = r":\s"   # ": "
    pattern = date_time + dash_whitespace + username + metadata_end

    with open(chat_export_file, "r", encoding="utf-8") as corpus_life:
        content = corpus_life.read()

    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))

def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]   #remove primeira e ultima linha
    filter_out_msgs = ("<Media omitted>",)
    return tuple(msg for msg in messages if msg not in filter_out_msgs)

def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus
