'''
Task 1: Keyword Highlighter
Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

python_review_1 = "This product is really good. I'm impressed with its quality." 
python_review_2 = "The performance of this product is excellent. Highly recommended!"
python_review_3 = "I had a bad experience with this product. It didn't meet my expectations."
python_review_4 = "Poor quality product. Wouldn't recommend it to anyone."
python_review_5 = "The product was average. Nothing extraordinary about it."
print(python_review_1.find("good")).upper

Task 2: Sentiment Tally
Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
total_positive = 0
total_negative = 0
if ?????:
   total_positive += 1
if ???:
   total_negative += 1
print(f"The total number of positive words is {total_positive}.")
print(f"The total number of negative words is {total_negative}.)

Task 3: Review Summary
Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

summary_python_review_1 = python_review_1[0,30] + "..."
summary_python_review_2 = python_review_2[0,30] + "..."
summary_python_review_3 = python_review_3[0,30] + "..."
summary_python_review_4 = python_review_4[0,30] + "..."
summary_python_review_5 = python_review_5[0,30] + "..."

How to make it not cut off in the middle of a word?

'''


    