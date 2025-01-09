# **Information Retrieval System**

A Python-based Information Retrieval System built for handling text data efficiently. This project implements Boolean retrieval and phrase query processing with indexing techniques for fast and accurate document searches.

---

## **Features**  
- **Inverted Index Construction**: Maps terms to documents for efficient retrieval.  
- **Positional Index Construction**: Supports phrase query search by storing term positions.  
- **Boolean Retrieval**: Handles queries using logical operators (`AND`, `OR`, `NOT`).  
- **Phrase Query Search**: Searches for exact phrases in documents.  
- **Text Preprocessing**: Includes tokenization, stopword removal, stemming, and punctuation handling.

---

## **Technologies Used**  
- **Python**: Core programming language for implementation.  
- **NLTK (Natural Language Toolkit)**: Used for text preprocessing (tokenization, stemming, and stopword removal).  

---

## **How to Use the System**

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/alim9hamed/FCAI-Projects.git
   cd FCAI-Projects
   ```

2. **Install Dependencies**  
   Make sure you have Python installed. Then install NLTK:
   ```bash
   pip install nltk
   ```

3. **Run the Script**  
   ```bash
   python main.py
   ```

4. **Input Documents**  
   - Enter the number of documents.  
   - Provide the text for each document.

5. **Choose Query Type**  
   - **Boolean Query**: Use logical operators (`AND`, `OR`, `NOT`).  
   - **Phrase Query**: Enter a phrase to search for exact matches.

---

## **Sample Output**

- **Inverted Index**  
  ```plaintext
  term1: {1, 2, 3}
  term2: {2, 3}
  ```

- **Positional Index**  
  ```plaintext
  term1: {1: [0, 2], 2: [1]}
  term2: {2: [0], 3: [1]}
  ```

- **Query Results**  
  ```plaintext
  Boolean Query: "term1 AND term2"
  Matching Documents: Document 2

  Phrase Query: "sample phrase"
  Matching Documents: Document 3
  ```

---

## **File Structure**

```
.
├── Information-Retrieval-System/
│   ├── README.md  # Detailed description of the Information Retrieval System
│   └── main.py    # Implementation script for the system
├── README.md       # Main description of the FCAI Projects repository
└── (Other projects as they are added)
```

---

## **Acknowledgments**

This project was developed as part of the **Information Retrieval** course under the guidance of:  
- **Dr. Rasha M. Badry**  
- **Eng. Azza A. Mohammed**  

---



## **Team Members**  

- **Ali Mohamed**  
- **Beltagy Mohamed**  
- **Abdelrahman Ramadan**  
- **Mahmoud El-Gohary**  
- **Shehab Salama**  
- **Abdelrahman Ghoneim**  

---

## **Contributing**  
Contributions are welcome! Feel free to fork the repository and submit a pull request.  
