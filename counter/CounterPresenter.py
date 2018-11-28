class CounterPresenter:
    def __init__(self, counter_model, view):
        self.counter_model = counter_model
        self.view = view

    def increment(self):
        new_count = self.counter_model.increment()
        self.view.show_count(new_count)

    def decrement(self):
        new_count = self.counter_model.decrement()
        self.view.show_count(new_count)
