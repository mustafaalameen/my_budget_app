print ('********YOUR FAVOURITE BUDGET APP********')
class Budget:

	def __init__(self, food, transport, clothing, entertainment):
		self.food=food
		self.transport=transport
		self.clothing=clothing
		self.entertainment=entertainment

	def deposit(self, amount, category):
		if 'food'== category:
			self.food+=amount
		elif 'transport'==category:
			self.transport+=amount
		elif 'clothing'== category:cler
			self.clothing+=amount
		elif 'entertainment'== category:
			self.entertainment+=amount
		print(f'You just deposited NGN {amount} to the {category}.' )
		
	def withdraw(self, amount, category):
		if 'food'== category:
			self.food-=amount
		elif 'transport'==category:
			self.transport-=amount
		elif 'clothing'== category:
			self.clothing-=amount
		elif 'entertainment'== category:
			self.entertainment-=amount
		print(f"You just withdraw NGN{amount} from {category}")
		
	def check_balance(self, category):
		if 'food'== category:
			balance=self.food
		elif 'transport'==category:
			balance=self.transport
		elif 'clothing'== category:
			balance=self.clothing
		elif 'entertainment'== category :
			balance=self.entertainment
		print(f"Your balance from the {category} category: NGN {balance}")
			
	def tansfer(self):
		
		pass

budget1=Budget(0,0,0,0)

# budget2=Budget(0,0,0,0)

def continue_budget():
	continue2Budget=int(input('\n\tDo you want to continue?\t 1. Yes 2. No\n'))
	if continue2Budget==1:
		init()
	else:
		print('Weldone!!!')
		exit()
		
def init():
	print 
	operation=int(input('1. Deposit 2. Withdraw 3. Check balance\n'))
	category=input('Type one this categgories>>> food---clothing---transport---entertainment\n')
	if operation==1:
		amount=int(input('How much are you depositing:\n'))
		budget1.deposit(amount, category)
	elif operation==2:
		amount=int(input('How much are you withdrawing:\n'))
		budget1.withdraw(amount, category)
	elif operation==3:
		budget1.check_balance(category)
	else:
		print('You selected an invalid option')
		exit()
	continue_budget()
init()