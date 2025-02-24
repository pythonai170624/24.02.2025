# stock_observer/main.py

from stock_grabber import StockGrabber
from stock_observers import StockObserver


def main():
    grabber = StockGrabber()

    observer1 = StockObserver("Smart Person", grabber)
    observer2 = StockObserver("Rich Person", grabber)

    grabber.set_ibm_price(101.5)
    grabber.set_apple_price(88.6)
    grabber.set_google_price(43.2)

    # grabber.unregister(observer2)
    del observer2

    grabber.set_google_price(50.0)


if __name__ == "__main__":
    main()
