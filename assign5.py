
import pandas as pd

# Q1: Build Personalized Knowledge Base

ROLL_NO = "1024170043"

# Take the last two digits
last_two_digits = [int(d) for d in ROLL_NO[-2:]]
print(last_two_digits)

categories = ["billing", "account", "general"]

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

# Personalized entries
personalized_entries = []

for d in last_two_digits:
    category = categories[d % 3]

    if category == "billing":
        question = "how can i check my payment status"
        answer = "You can check your payment status from the Billing section."
        keywords = "payment status transaction billing"

    elif category == "account":
        question = "how do i update my registered mobile number"
        answer = "Go to Account Settings and update your registered mobile number."
        keywords = "mobile number update account"

    else:
        question = "how can i contact customer support"
        answer = "You can contact customer support through the Help section."
        keywords = "support help contact"

    personalized_entries.append({
        "question": question,
        "answer": answer,
        "keywords": keywords,
        "category": category
    })

# Combine fixed + personalized entries
all_entries = fixed_entries + personalized_entries

df = pd.DataFrame(all_entries)

print("Q1: Final 6-row DataFrame")
print(df)
print()

# Q2: Generate and Score a Hypothesis

def score_query(query, df):
    query_words = set(query.lower().split())

    results = []

    for index, row in df.iterrows():

        # Convert keywords into individual words
        keyword_words = set(row["keywords"].lower().split())

        # Count matching words
        matches = query_words.intersection(keyword_words)

        # Confidence score
        score = len(matches)

        if score > 0:
            results.append({
                "index": index,
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score,
                "matched_keywords": ", ".join(matches)
            })

    # Sort highest score first
    results.sort(key=lambda x: x["score"], reverse=True)

    return results


query = "fee payment"

print("Q2: Scoring query:", query)

results = score_query(query, df)

for result in results:
    print(result)

print()

# Q3: same_category(category_name, df)

def same_category(category_name, df):
    return df[df["category"].str.lower() == category_name.lower()]


# Use the category of the first personalized entry
personalized_category = personalized_entries[0]["category"]

print("Q3: Entries belonging to category:", personalized_category)

category_result = same_category(personalized_category, df)

print(category_result)
print()

# Q4: Add a new keyword and save CSV

print("Q4: Current knowledge base")
print(df)

# Pick the first entry
entry_index = 0

new_keyword = input("Enter a new keyword to add to the first FAQ entry: ")

# Add the new keyword
df.loc[entry_index, "keywords"] = (
    df.loc[entry_index, "keywords"] + " " + new_keyword
)

# Save the complete updated DataFrame
filename = ROLL_NO + "_faq_data.csv"

df.to_csv(filename, index=False)

print("\nUpdated entry:")
print(df.loc[entry_index])

print("\nEntire DataFrame saved to:", filename)
print()

# Q5: Count FAQ entries per category using groupby

print("Q5: Number of FAQ entries per category")

category_counts = df.groupby("category").size()

print(category_counts)
print()

# Q6: Modified scoring function with tie handling

def score_query_with_ties(query, df):

    query_words = set(query.lower().split())

    results = []

    for index, row in df.iterrows():

        keyword_words = set(row["keywords"].lower().split())

        matches = query_words.intersection(keyword_words)

        score = len(matches)

        if score > 0:
            results.append({
                "index": index,
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score,
                "matched_keywords": ", ".join(matches)
            })

    if not results:
        print("No matching entries found.")
        return

    # Highest score
    highest_score = max(result["score"] for result in results)

    # Get ALL entries having highest score
    best_matches = [
        result for result in results
        if result["score"] == highest_score
    ]

    print("\nQuery:", query)
    print("Highest confidence score:", highest_score)

    if len(best_matches) > 1:
        print("TIE DETECTED! Multiple equally good matches:\n")
    else:
        print("Unique best match:\n")

    for result in best_matches:
        print("Question:", result["question"])
        print("Answer:", result["answer"])
        print("Category:", result["category"])
        print("Score:", result["score"])
        print("Matched keywords:", result["matched_keywords"])
        print("-" * 50)


# Q6 Demo 1

score_query_with_ties("fee", df)

# Q6 Demo 2

score_query_with_ties("password", df)
[5, 5]
Q1: Final 6-row DataFrame
                             question  \
0              what is the annual fee   
1               how to reset password   
2         what are your working hours   
3               how can i pay the fee   
4  how can i contact customer support   
5  how can i contact customer support   

                                              answer                keywords  \
0                          The annual fee is Rs 500.   fee cost price charge   
1                   Go to Settings > Reset Password.    password reset login   
2                          We are open 9 AM to 5 PM.  hours timing open time   
3         You can pay via UPI, card, or net banking.     pay payment upi fee   
4  You can contact customer support through the H...    support help contact   
5  You can contact customer support through the H...    support help contact   

  category  
0  billing  
1  account  
2  general  
3  billing  
4  general  
5  general  

Q2: Scoring query: fee payment
{'index': 3, 'question': 'how can i pay the fee', 'answer': 'You can pay via UPI, card, or net banking.', 'category': 'billing', 'score': 2, 'matched_keywords': 'fee, payment'}
{'index': 0, 'question': 'what is the annual fee', 'answer': 'The annual fee is Rs 500.', 'category': 'billing', 'score': 1, 'matched_keywords': 'fee'}

Q3: Entries belonging to category: general
                             question  \
2         what are your working hours   
4  how can i contact customer support   
5  how can i contact customer support   

                                              answer                keywords  \
2                          We are open 9 AM to 5 PM.  hours timing open time   
4  You can contact customer support through the H...    support help contact   
5  You can contact customer support through the H...    support help contact   

  category  
2  general  
4  general  
5  general  

Q4: Current knowledge base
                             question  \
0              what is the annual fee   
1               how to reset password   
2         what are your working hours   
3               how can i pay the fee   
4  how can i contact customer support   
5  how can i contact customer support   

                                              answer                keywords  \
0                          The annual fee is Rs 500.   fee cost price charge   
1                   Go to Settings > Reset Password.    password reset login   
2                          We are open 9 AM to 5 PM.  hours timing open time   
3         You can pay via UPI, card, or net banking.     pay payment upi fee   
4  You can contact customer support through the H...    support help contact   
5  You can contact customer support through the H...    support help contact   

  category  
0  billing  
1  account  
2  general  
3  billing  
4  general  
5  general  
Enter a new keyword to add to the first FAQ entry:  billing
Updated entry:
question           what is the annual fee
answer          The annual fee is Rs 500.
keywords    fee cost price charge billing
category                          billing
Name: 0, dtype: str

Entire DataFrame saved to: 1024170255_faq_data.csv

Q5: Number of FAQ entries per category
category
account    1
billing    2
general    3
dtype: int64


Query: fee
Highest confidence score: 1
TIE DETECTED! Multiple equally good matches:

Question: what is the annual fee
Answer: The annual fee is Rs 500.
Category: billing
Score: 1
Matched keywords: fee
--------------------------------------------------
Question: how can i pay the fee
Answer: You can pay via UPI, card, or net banking.
Category: billing
Score: 1
Matched keywords: fee
--------------------------------------------------

Query: password
Highest confidence score: 1
Unique best match:

Question: how to reset password
Answer: Go to Settings > Reset Password.
Category: account
Score: 1
Matched keywords: password
--------------------------------------------------
 
