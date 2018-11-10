class CacheObserver:

    def update(self, data):
        print("Odswieza cache - dodano: " + data)


class RSSObserver:

    def update(self, data):
        print("Odswieza RSS - dodano: " + data)


class NewsletterObserver:

    def update(self, data):
        print("Odswieza Newsletter - dodano: " + data)


class News:

    def __init__(self):
        self.__observers = []

    def attach_observer(self, observer):
        self.__observers.append(observer)

    def detach_observer(self, observer):
        self.__observers.remove(observer)

    def __notifyObservers(self, data):
        for observer in self.__observers:
            observer.update(data)

    def addData(self, data):
        print("Dodano dane " + data)
        self.__notifyObservers(data)


if __name__ == "__main__":
    news = News()
    cache_observer = CacheObserver()
    rss_observer = RSSObserver()
    newsletter_observer = NewsletterObserver()

    news.attach_observer(cache_observer)
    news.attach_observer(rss_observer)
    news.attach_observer(newsletter_observer)

    news.addData("DANE")
