class GetEnumValuesMixin:
    @classmethod
    def get_values(cls):
        return [(x.name, x.value) for x in cls]


class GetEnumMaxLenValueMixin:
    @classmethod
    def get_longer_value(cls):
        return max(len(x.value) for x in cls)

