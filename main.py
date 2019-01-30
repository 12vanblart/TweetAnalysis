####################
## 12vanblart ######
## Tweet Analysis ##
####################
import csvkit


def main():
    remainingTweets = 0
    replyTweets = 0
    androidTweets = 0
    webTweets = 0
    youtubeLikeTweets = 0
    reTweets = 0
    hashtaggedTweets = 0
    mentionTweets = 0
    imageTweets = 0
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
    csv_reader = csvkit.reader(csv_file)
    for row in csv_reader:
        if row == 0:
            # Do nothing
            print("Header Row")
        else:
            remainingTweets += 1
            if row[1] != "":
                replyTweets += 1
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("Tweet analytics")
    print("###############")
    print("Total non-deleted Tweets: ", remainingTweets)
    print("This means you deleted",
          "{0:.2f}".format(100 - (100 * remainingTweets/totalTweets)), "% of your total tweets")
    print("###############")
    print("You replied in", replyTweets, "tweets")
    print("This translates to", "{0:.2f}".format(
        (100 * replyTweets/totalTweets)), "% of your total tweets")
    csv_file.close()


if __name__ == "__main__":
    main()
