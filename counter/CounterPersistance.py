import json


class CounterPersistance:
    def persist(self, count):
        pass

    def load(self):
        return 0


class CounterPersistanceImpl(CounterPersistance):

    def persist(self, count):
        with open('data.json', 'w') as outfile:
            json.dump( { "count": count }, outfile )

    def load(self):
        with open('data.json', 'r') as outfile:
            return json.load(outfile)["count"]
