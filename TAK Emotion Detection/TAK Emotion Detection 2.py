from textblob import TextBlob

feedback=input("Cümleyi giriniz: ")
feedback_polarity = TextBlob(feedback).sentiment.polarity

if feedback_polarity>0:
    print("cümle pozitif")
elif feedback_polarity<0:
    print("cümle negatif")
