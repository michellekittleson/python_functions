#Task 1: Keyword Highlighter
#Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

list_of_keywords = ["good", "excellent", "bad", "poor", "average"]

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
python_reviews_lower = []

for review in python_reviews:
   review = review.replace(".", "")
   python_reviews_lower.append(review.lower())

print(python_reviews_lower)
python_reviews2 = python_reviews_lower
def keyword_highligher(list_of_reviews):
   new_python_reviews = []
   for review in list_of_reviews:
      for word in review.split():
         if word in list_of_keywords:
               review = review.replace(word, word.upper())
               new_python_reviews.append(review)
               print(new_python_reviews)
   return new_python_reviews
print(keyword_highligher(python_reviews_lower))
print(python_reviews2)

#Task 2: Sentiment Tally
#Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
total_positive = 0
total_negative = 0
for review in python_reviews2:
   for word in positive_words:
      if word in review:
         total_positive += 1
   for word in negative_words:
      if word in review:
         total_negative += 1

print(f"The total number of positive words is {total_positive}.")
print(f"The total number of negative words is {total_negative}.")

#Task 3: Review Summary
#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
for review in python_reviews:
    if review[30] == " ":
        review_summary = review[:30]
        print(review_summary + "...")
    elif review[29] == " ":
        review_summary = review[:29]
        print(review_summary + "...")
    elif review [28] == " ":
        review_summary = review[:28]
        print(review_summary + "...")
    elif review [27] == " ":
        review_summary = review[:27]
        print(review_summary + "...")
    elif review [26] == " ":
        review_summary = review[:26]
        print(review_summary + "...")
    elif review [25] == " ":
        review_summary = review[:25]
        print(review_summary + "...")
    elif review [24] == " ":
        review_summary = review[:24]
        print(review_summary + "...")
    elif review [23] == " ":
        review_summary = review[:23]
        print(review_summary + "...")