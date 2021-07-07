class Employee:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("Welcome")

	@classmethod
	def raise_amt(cls, amount):
		cls.raise_amt = amount


emp1 = Employee('Abideen', 12)
emp2 = Employee('Muhammed', 21)

print(emp1.name)
