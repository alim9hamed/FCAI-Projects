# IR Project: Boolean Retrieval Model Using Inverted and Positional Index

## Step 1: Building Inverted Index and Positional Index
def build_inverted_index(documents):
    inverted_index = {}

    for doc_id, doc_text in documents.items():
        words = doc_text.lower().split()
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = set()
            inverted_index[word].add(doc_id)

    return inverted_index

def build_positional_index(documents):
    positional_index = {}

    for doc_id, doc_text in documents.items():
        words = doc_text.lower().split()
        for position, word in enumerate(words):
            if word not in positional_index:
                positional_index[word] = {}
            if doc_id not in positional_index[word]:
                positional_index[word][doc_id] = []
            positional_index[word][doc_id].append(position)

    return positional_index

## Step 2: Processing Queries
def boolean_retrieval(query, inverted_index):
    query_terms = query.split()
    result = set()
    operation = None

    for term in query_terms:
        if term.lower() == 'and':
            operation = 'and'
        elif term.lower() == 'or':
            operation = 'or'
        elif term.lower() == 'not':
            operation = 'not'
        else:
            term = term.lower()
            term_result = inverted_index.get(term, set())

            if operation == 'and':
                result = result.intersection(term_result) if result else term_result
            elif operation == 'or':
                result = result.union(term_result)
            elif operation == 'not':
                result.difference_update(term_result)
            else:
                result = term_result

    return result

def phrase_query(phrase, positional_index):
    query_words = phrase.lower().split()
    if query_words[0] not in positional_index:
        return set()

    result = set(positional_index[query_words[0]].keys())
    for i in range(1, len(query_words)):
        word = query_words[i]
        if word not in positional_index:
            return set()

        temp_result = set()
        for doc_id in result:
            positions_prev_word = positional_index[query_words[i - 1]].get(doc_id, [])
            positions_current_word = positional_index[word].get(doc_id, [])
            for pos in positions_prev_word:
                if pos + 1 in positions_current_word:
                    temp_result.add(doc_id)
                    break
        result = temp_result

    return result

## Main Functionality
if __name__ == "__main__":
    # Input documents
    num_documents = int(input("Enter the number of documents: "))
    documents = {}

    for i in range(1, num_documents + 1):
        doc_text = input(f"Enter words for Document {i}: ")
        documents[i] = doc_text

    # Build indexes
    inverted_index = build_inverted_index(documents)
    positional_index = build_positional_index(documents)

    # Print indexes
    print("\nInverted Index:")
    for term, posting_list in inverted_index.items():
        print(f"{term}: {posting_list}")

    print("\nPositional Index:")
    for term, postings in positional_index.items():
        print(f"{term}: {postings}")

    # Query processing
    while True:
        query_type = input("\nEnter query type (boolean/phrase/exit): ").lower()

        if query_type == "boolean":
            query = input("Enter your Boolean query: ")
            result = boolean_retrieval(query, inverted_index)
            if result:
                print("Matching Documents:")
                for doc_id in result:
                    print(f"Document {doc_id}: {documents[doc_id]}")
            else:
                print("No matching documents found.")

        elif query_type == "phrase":
            phrase = input("Enter your phrase query: ")
            result = phrase_query(phrase, positional_index)
            if result:
                print("Matching Documents:")
                for doc_id in result:
                    print(f"Document {doc_id}: {documents[doc_id]}")
            else:
                print("No matching documents found.")

        elif query_type == "exit":
            print("Exiting...")
            break

        else:
            print("Invalid query type. Please enter 'boolean', 'phrase', or 'exit'.")
