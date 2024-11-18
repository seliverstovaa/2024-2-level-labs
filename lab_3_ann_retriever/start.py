"""
Laboratory Work #3 starter.
"""

# pylint:disable=duplicate-code, too-many-locals, too-many-statements, unused-variable
from pathlib import Path

from lab_3_ann_retriever.main import BasicSearchEngine, SearchEngine, Tokenizer, Vectorizer


def open_files() -> tuple[list[str], list[str]]:
    """
    # stubs: keep.

    Open files.

    Returns:
        tuple[list[str], list[str]]: Documents and stopwords
    """
    documents = []
    for path in sorted(Path("assets/articles").glob("*.txt")):
        with open(path, "r", encoding="utf-8") as file:
            documents.append(file.read())
    with open("assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    return (documents, stopwords)


def main() -> None:
    """
    Launch an implementation.
    """
    with open("assets/secrets/secret_1.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()
    documents, stopwords = open_files()

    tokenizer = Tokenizer(stopwords)
    tokenized_docs = tokenizer.tokenize_documents(documents)

    if not isinstance(tokenized_docs, list):
        result = None
    vectorizer = Vectorizer(tokenized_docs)
    docs_vector = [vectorizer.vectorize(tokens) for tokens in tokenized_docs]

    query = 'Нижний Новгород'
    knn_retriever = BasicSearchEngine(vectorizer=vectorizer, tokenizer=tokenizer)
    knn_retriever.index_documents(documents)
    print(knn_retriever.retrieve_relevant_documents(query, 3))

    naive_kdtree_retriever = SearchEngine(vectorizer, tokenizer)
    naive_kdtree_retriever.index_documents(documents)
    print(naive_kdtree_retriever.retrieve_relevant_documents(query))

    result = None
    assert result, "Result is None"


if __name__ == "__main__":
    main()
