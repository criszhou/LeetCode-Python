from collections import defaultdict

class Twitter(object):
    feedSize = 10

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followeeMap = defaultdict(set) # maps a person P to the set { Q | P follows Q }
        self.tweetRankMap = defaultdict(list) # maps a person to the list of tweet ranks of him
        self.tweetRankToID = dict() # maps a rank to the tweet id. Need this because higher tweet id does not guarantee it's later
        self.nextTweetRank = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweetRankMap[ userId ].append( self.nextTweetRank )
        self.tweetRankToID[ self.nextTweetRank ] = tweetId
        self.nextTweetRank += 1

        # just to save time, not absolutely necessary
        if len(self.tweetRankMap[ userId ]) > 2 * self.feedSize:
            self.tweetRankMap[userId] = self.tweetRankMap[ userId ][-self.feedSize:]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        allTweetRanks = self.tweetRankMap[ userId ][-self.feedSize:]
        for followeeId in self.followeeMap[ userId ]:
            allTweetRanks.extend( self.tweetRankMap[ followeeId ][-self.feedSize:] )
        allTweetRanks.sort()
        newTweetRanks = allTweetRanks[-1:-self.feedSize-1:-1]

        return [ self.tweetRankToID[r] for r in newTweetRanks ]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.followeeMap[ followerId ].add( followeeId )

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.followeeMap[ followerId ]:
            self.followeeMap[ followerId ].remove( followeeId )



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)