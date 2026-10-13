class SocialMedia:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getFollowers(self):
        return self.followers

    def setFollowers(self, followers):
        self.followers = followers

    def cal(self):
        print("Followers =", self.followers)

    def display(self):
        print("Username =", self.username)
        print("Followers =", self.followers)


class Instagram(SocialMedia):
    def __init__(self, username, followers, likes):
        super().__init__(username, followers)
        self.likes = likes

    def cal(self):
        print("Instagram engagement =", self.likes / self.followers * 100, "%")

    def display(self):
        super().display()
        print("Likes =", self.likes)


class YouTube(SocialMedia):
    def __init__(self, username, followers, views):
        super().__init__(username, followers)
        self.views = views

    def cal(self):
        print("YouTube views per follower =", self.views / self.followers)

    def display(self):
        super().display()
        print("Views =", self.views)


s1 = SocialMedia("Sakshi", 100)
i1 = Instagram("Sakshi_123", 500, 100)
y1 = YouTube("SakshiVlogs", 1000, 5000)

s1.cal()
i1.cal()
y1.cal()
