import os
import pandas as pd
from datetime import datetime, date, time
const = "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
class Virtual_bank():

	def sheet_add(str_name = "1", column_name="", text="0", file = "sheet"):
		df = pd.read_csv(str(os.getcwd()) + "\\" + str(file))
		df.loc[[0], "баланс"] = text
		df.to_csv(file, encoding='utf-8', index=False)
		print(df)
		return df

	def open_sheet(self):
		sheet_num = "sheet"
		df = pd.read_csv(str(os.getcwd()) + "\\" + str(sheet_num))
		count_money = int(df.loc[0, 'баланс'])
		sum_money = count_money + df["доход/расход в рублях"].sum(axis=0)
		print(sum_money)

	def balance(self):
		df = self.check_player_sheet()
		print(df)
		balance = input("Введите свой стартовый баланс>>> ")
		df = self.sheet_add(column_name="баланс", text=balance)
		df.to_csv(str("sheet"), encoding='utf-8', index=False)

	def calculation(self, file = "sheet"):

		print("Для записи дохода пишите положительные числа, а для записи расхода пишите отрицательные числа ")

		s = input("Введите доход или расход>>> ")
		predict = input("Введите причину расхода или дохода>>> ")
		time = datetime.now()
		df = pd.read_csv(str(os.getcwd()) + "\\" + str(file))
		df = df.append({"доход/расход в рублях": s, "причина расхода или дохода": predict, "time_reg": str(time)[:16]}, ignore_index=True)
		df.to_csv(str(file), encoding='utf-8', index=False)
		print(df)
	def check_player_sheet(self):
		id_user = "sheet"
		path = str(os.getcwd())
		if id_user in os.listdir(path):
			print("открываем файл логирования данных действий игроков")
		else:
			df =  data = {
			"time_reg": [0],
			"доход/расход в рублях": [0],
			"причина расхода или дохода" : [0] ,
			"баланс" : [0]
			} # Этот столбец отвечет за указание порядкового номера вопроса на котором остановился юзер
			frame = pd.DataFrame(data)
			frame.to_csv(id_user, index=False)
			print("Файл логирования данных действий финансистов не найден")
			print("Создаю файл логирования данных действий финансистов")
			print(frame)
		return id_user


	def bank_create_folder(self, path = ""): #Функция создает папку для бух учета если ее нет
		path = str(os.getcwd())
		if "Virtual_accounting_folder" in os.listdir(path):
			os.chdir(path + "\\" + "Virtual_accounting_folder")
			print("Папка уже создана")
		else:
			os.makedirs("Virtual_accounting_folder")
			print("Создаю папку для данных виртуального учета денег")

			self.bank_create_folder()

bank = Virtual_bank()
bank.bank_create_folder()
bank.check_player_sheet()

def menu():
	print("1 - Ввести баланс")
	print("2 - Внести расходы или доходы")
	print("3- Проверить баланс c учетом расходов и доходов ")
	key = int(input("Введите значение>>> "))
	if key == 1:
		print(const)
		bank.balance()
		print(const)
	elif key == 2:
		print(const)
		bank.calculation()
		print(const)
	elif key == 3:
		print(const)
		print("Итоговый баланс с вычетом рассходов и доходов :")
		bank.open_sheet()
		df = pd.read_csv(str(os.getcwd()) + "\\" + str("sheet"))
		print(df)
		print(const)
	else:
		print("Не верная функция")
	menu()
menu()