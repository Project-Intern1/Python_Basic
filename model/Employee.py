class Employee:
    def __init__(self,id, gender,birthday, address, fullName,idCard,phone):
        self._id = id
        self._gender = gender
        self._birthday = birthday
        self._address = address
        self._fullName = fullName
        self._idCard = idCard
        self._phone = phone

    @property
    def id(self):
        return self._id


    @id.setter
    def id(self, value):
        self._id = value

    @property
    def gender(self):
        return self._gender

    # Setter cho tên
    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def birthday(self):
        return self._birthday

    # Setter cho tên
    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @property
    def address(self):
        return self._address

    # Setter cho tên
    @address.setter
    def address(self, value):
        self._address = value

    @property
    def fullName(self):
        return self._fullName

    # Setter cho tên
    @fullName.setter
    def fullName(self, value):
        self._fullName = value

    @property
    def idCard(self):
        return self._idCard

    # Setter cho tên
    @idCard.setter
    def idCard(self, value):
        self._idCard = value

    @property
    def phone(self):
        return self._phone

    # Setter cho tên
    @phone.setter
    def phone(self, value):
        self._phone = value
    def list_inf(self):
        print("Employee ID:", self._id)
        print("Giới tính:", self._gender)
        print("Ngày sinh:", self._id)
        print("Employee ID:", self._id)
        print("Employee ID:", self._id)
        print("Employee ID:", self._id)
        print("Employee ID:", self._id)

