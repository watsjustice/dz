import re
import asyncio

class Math:

	__final , __type = int() , str()

	__slots__ = ['_value']

	def __init__(self , *kwargs):
		globals().update({item : object for item , object in zip(['value_' + str(x) for x in range(1,1000)] , kwargs)})
		self._value = value_1

	@property
	def addiction(self):
		Math.__type = 'Addiction'
		Math.__final = eval('+'.join(list(globals())[16:]))
		return Math.__final
	@property
	def multiplication(self):
		Math.__type = 'Multiplication'
		Math.__final = eval('*'.join(list(globals())[16:]))
		return Math.__final
	@property
	def division(self):
		Math.__type = 'Division'
		Math.__final = eval('/'.join(list(globals())[16:]))
		return Math.__final
	@property
	def pow(self):
		Math.__type = 'Pow'
		Math.__final = eval('(' * (len(list(globals())[16:])-1) + re.sub(r'[*][*]\w+[_]\d' , r'\g<0>)' , '**'.join(list(globals())[16:]))) 
		return Math.__final
	@property
	def sqrt(self):
		Math.__type = 'Sqrt'
		Math.__final = eval('**0.5'.join(list(globals())[16:]))
		return Math.__final

	@staticmethod
	def typeAccessforeq(value):
		if isinstance(value , int):
			return value
		else:
			raise TypeError ('Uncorrect input')

	def __str__(self):
		return f'{Math.__type} : {Math.__final}'




class Sort(Math):

	__slots__ = ['length']

	def __init__(self , _value):
		super().__init__(_value)
		self.length = len(self._value)
		Sort.typeAccess(self._value)

	@property
	def bublesortin(self):
		for i in range(0 ,self.length):
			for j in range(0 , self.length - i - 1):
				if self._value[j] > self._value[j + 1]:
					temp = self._value[j]
					self._value[j] = self._value[j + 1]
					self._value[j + 1] = temp
		return self._value

	@staticmethod
	def typeAccess(value):
		if isinstance(value , list):
			return value
		else:
			raise TypeError ('Uncorrect input')

	def __str__(self):
		return f"The buble sortin : {self._value}" 





async def main():
	task1 = asyncio.create_task(mathoperation(2,3,5,6))
	task2 = asyncio.create_task(timerequired())
	await task1


async def mathoperation(*kwargs):
	x = Math(*kwargs)
	await asyncio.sleep(1.1)
	x.pow
	print('\n'*10)
	print(x)

async def timerequired():
	for i in range(10000):
		await asyncio.sleep(0.25)
		print(f'Calculating , time passed {i}...')

asyncio.run(main())
