from textblob import TextBlob

feedbacks = ["I love you so much",
             "Such a good thing",
             "I will kil you",
             "I feel like blue today",
             "This meats like shit",
             "You are not a good person",]

positive=[]
negative=[]

for feedback in feedbacks:
    feedback_polarity = TextBlob(feedback).sentiment.polarity
    if feedback_polarity>0:
        positive.append(feedback)
        continue
    negative.append(feedback)

print("Positif {} adet cümle bulundu.".format(len(positive)))
print(positive)
print("Negatif {} adet cümle bulundu.".format(len(negative)))
print(negative)