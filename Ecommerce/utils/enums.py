import enum

from Ecommerce.utils.model_mixins import GetEnumValuesMixin, GetEnumMaxLenValueMixin


class GenderEnum(GetEnumValuesMixin, GetEnumMaxLenValueMixin, enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'
