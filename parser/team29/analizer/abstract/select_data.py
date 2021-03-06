import pandas as pd



class dataSelect():

	dataTable = None

	def __init__(self):
		self.customer = pd.read_csv("C:\\Users\\momob\\OneDrive\\Documentos\\OLC2_DOCS\\OLC2_PROYECTO_DOCS\\analizer\\abstract\\customer.csv") 
		self.product = pd.read_csv("C:\\Users\\momob\\OneDrive\\Documentos\\OLC2_DOCS\\OLC2_PROYECTO_DOCS\\analizer\\abstract\\product.csv") 
		self.purchase = pd.read_csv("C:\\Users\\momob\\OneDrive\\Documentos\\OLC2_DOCS\\OLC2_PROYECTO_DOCS\\analizer\\abstract\\purchase.csv") 
		self.tables = [self.customer, self.product, self.purchase]
		# print(self.customer)
		# print("\n")
		# print(self.product)
		# print("\n")
		# print(self.purchase)

	def crossJoin(self):
		if len(self.tables) <= 1 : return
		for t in self.tables : t['____tempCol'] = 1

		new_df = self.tables[0]
		i=1
		while i < len(self.tables):
			new_df = pd.merge(new_df,self.tables[i], on=['____tempCol'])
			i+=1

		new_df = new_df.drop('____tempCol', axis=1)
		self.dataTable = new_df
		# print(new_df.head(10))
		# print(new_df.columns.values)
