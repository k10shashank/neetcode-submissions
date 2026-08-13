import heapq

class Twitter:

    def __init__(self):
        self.tweets = dict()
        self.follows = dict()
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.tweets.get(userId) is None:
            self.tweets[userId] = []
            self.follows[userId] = {userId}
        heapq.heappush(self.tweets[userId], (self.counter, tweetId))
        self.counter += 1
        if len(self.tweets[userId]) > 10:
            heapq.heappop(self.tweets[userId])


    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for followId in self.follows[userId]:
            for tweetId in self.tweets[followId]:
                heapq.heappush(tweets, (-tweetId[0], tweetId[1]))
        output = []
        while len(output) < 10 and len(tweets) > 0:
            output.append(heapq.heappop(tweets)[1])
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if self.tweets.get(followerId) is None:
            self.tweets[followerId] = []
            self.follows[followerId] = {followerId}
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
