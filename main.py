####################
## 12vanblart ######
## Tweet Analysis ##
####################
import csv
from collections import Counter
import re


def main():
    remainingTweets = 0
    replyTweets = 0
    reTweets = 0
    hashtaggedTweets = 0
    mentionTweets = 0
    imageTweets = 0
    interfaceCollection = []
    print("--------------------------------------------")
    print("Tweet Anlaysis Time!")
    print("--------------------------------------------")
    print("First things first!")
    print("Unzip your twitter export and rename the folder to to `tweets` ")
    print("Then place the folder in the same location as this program")
    #input("Press Enter once completed")
    totalTweets = int(input(
        "How many total tweets does your profile show (number, no commas)? "))
    csv_file = open('./tweets/tweets.csv', 'r', encoding='utf-8')
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row == 0:
            # Do nothing
            print("Header Row")
        else:
            remainingTweets += 1
            if row[1] != "":
                replyTweets += 1
            if row[6] != "":
                reTweets += 1
            try:
                found = re.search('">(.+?)</a', row[4]).group(1)
            except:
                found = ''
            interfaceCollection.append(found)
            try:
                foundAt = re.search('@', row[5])
                if foundAt:
                    mentionTweets += 1
            except:
                found = ''
            try:
                foundHashtag = re.search('#', row[5])
                if foundHashtag:
                    hashtaggedTweets += 1
            except:
                found = ''
            try:
                foundImage = re.search('/photo/', row[9])
                if foundImage:
                    imageTweets += 1
            except:
                found = ''

    # Count values from list
    commonInterface = Counter(interfaceCollection).most_common()
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("Tweet analytics")
    print("###############")
    print("Total non-deleted Tweets: ", remainingTweets)
    print("This means you deleted",
          "{0:.2f}".format(100 - (100 * remainingTweets/totalTweets)), "% of your total tweets")
    print("###############")
    print("You replied in", replyTweets, " of your tweets")
    print("This translates to", "{0:.2f}".format(
        (100 * replyTweets/totalTweets)), "% of your total tweets")
    print("###############")
    print("You retweeted", reTweets, "tweets")
    print("This translates to", "{0:.2f}".format(
        (100 * reTweets/totalTweets)), "% of your total tweets")
    print("###############")
    print("You mentioned somone in", mentionTweets, "of your tweets")
    print("This translates to", "{0:.2f}".format(
        (100 * mentionTweets/totalTweets)), "% of your total tweets")
    print("###############")
    print("You used at least one hashtag in",
          hashtaggedTweets, "of your tweets")
    print("This translates to", "{0:.2f}".format(
        (100 * hashtaggedTweets/totalTweets)), "% of your total tweets")
    print("###############")
    print("Images appeared in", imageTweets, "of your tweets")
    print("This translates to", "{0:.2f}".format(
        (100 * imageTweets/totalTweets)), "% of your total tweets")
    print("###############")
    print("Your tweet breakdown by platform of origin:")
    for i in range(len(commonInterface)):
        print(str(i+1), ": ", str(commonInterface[i][0]).strip(), ": ", "{0:.2f}".format(
            (100*commonInterface[i][1]/totalTweets)), "%", sep="")

    csv_file.close()


if __name__ == "__main__":
    main()
