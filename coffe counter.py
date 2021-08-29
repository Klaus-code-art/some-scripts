
import datetime
import pandas as pd


market_list = []
check_list = {}

#Функция принимающая наименование покупок сохраняющая их список 
def market_names(market_list = market_list):
  n = 0
  a = input("запишите покупку либо проболжите либо прервите >>>  ")
  if a.lower() == "капучино 0.3":
    market_list.append(a)
  elif a.lower() == "капучино 0.4":
    market_list.append(a)
  elif a.lower() == "латте 0.3":
    market_list.append(a)
  elif a.lower() == "латте 0.4":
    market_list.append(a)
  elif a.lower() == "американо ":
    market_list.append(a)
  elif a.lower() == "флет":
    market_list.append(a)
  elif a.lower() == "файнфлет":
    market_list.append(a)
  elif a.lower() == "раф 0.3":
    market_list.append(a)
  elif a.lower() == "раф 0.4":
    market_list.append(a)
  elif a.lower() == "эспрессо":
    market_list.append(a)
  elif a.lower() == "шот":
    market_list.append(a)
  elif a.lower() == "двойной эспрессо":
    market_list.append(a)
  elif a.lower() == "фреш":
    market_list.append(a)
  elif a.lower() == "какао 0.3":
    market_list.append(a)
  elif a.lower() == "какао 0.4":
    market_list.append(a)
  elif a.lower() == "сироп":
    market_list.append(a)
  elif a.lower() == "альтернатианое молоко":  
    market_list.append(a)
  elif a.lower() == "альтернатианое молоко":  
    market_list.append(a)
  elif a.lower() == "чай 0.3":  
    market_list.append(a)
  elif a.lower() == "чай 0.4":  
    market_list.append(a)
  elif a.lower() == "рассчет":  
    print("расчет стоимости покупки")
    n = 1
    market_check(market_list = market_list)
  elif a.lower() == "очистить":  
    print("операция прервана, корзина очищена")
    market_list.clear()
    check_list.clear()
    n == 1
  else:
    print("значение не предусмотрено")
  if n == 0:
    market_names(market_list = market_list)
  else:
    print("производится формирование таблицы")

# функция принимающая и суммирующая значения корзины 
def market_check(market_list = market_list):
  print(len(market_list), "покупок")

  for i in market_list:
    if (i == "капучино 0.3") or (i == "латте 0.3"):
      check_list[i] = 190
    elif (i == "капучино 0.4") or (i == "латте 0.4"):
      check_list[i] = 230
    elif i == "американо ":
      check_list[i] = 130
    elif i == "флет":
      check_list[i] = 190
    elif i == "файнфлет":
      check_list[i] = 190
    elif i == "раф 0.3":
      check_list[i] = 210
    elif i  == "раф 0.4":
      check_list[i] = 250
    elif i == "эспрессо":
      check_list[i] = 100
    elif i == "шот":
      check_list[i] = 50
    elif i == "двойной эспрессо":
      check_list[i] = 150
    elif i == "фреш":
      check_list[i] = 250
    elif i == "какао 0.3" :
      check_list[i] = 150
    elif i == "какао 0.4":
      check_list[i] = 200
    elif i == "сироп":
      check_list[i] = 40
    elif i == "альтернатианое молоко":  
      check_list[i] = 80
    elif i == "чай 0.3":  
      check_list[i] = 150
    elif i == "чай 0.4":  
      check_list[i] = 200
    else:
      print("значение не предусмотрено")
  print(check_list )
  print("Сумма покупки корзины >>>  ", sum(check_list.values()), " рублей")

  sum_buys = sum(check_list.values())
  discount(sum_buys, market_list)

#Функция скидок 
def discount(sum_buys, market_list = market_list):
  print("производим рассчет скидки")
  admin_count = 0
  pref_name = str(input("введите категорию клиента >>>  "))
  if pref_name == "ученик":
    sum_buys_discount = sum_buys - (sum_buys * 0.1)
  elif pref_name == "преподаватель":
    sum_buys_discount = sum_buys - (sum_buys * 0.25)
  elif pref_name == "администратор":
    for i in market_list:
      if (i == "капучино 0.3") or (i == "латте 0.3") or (i == "капучино 0.4") or (i == "латте 0.4") or (i == "раф 0.4") or (i == "латте 0.4"):
        admin_count = admin_count + 100
      if (i == "альтернатианое молоко"):
        admin_count = admin_count + 50
    sum_buys_discount = admin_count
  else:
    sum_buys_discount = sum_buys
  print("С учетом скидки сумма покупки составляет >>> ", sum_buys_discount)

#функция записвающая все в таблицу покупки, стоимость, время создания корзины  и закрывающая корзину 
def input_base(check_list = check_list):
  product_names =[]
  sale = []
  time = []
  for i in check_list.keys():
    product_names.append(i)
  for a in check_list.values():
    sale.append(a)
    time.append(datetime.today())
  df = pd.DataFrame({'Дата, время': time, 'Наименование товара': product_names, 'Цена товара': sale})
  product_names.clear()
  sale.clear()
  return df


market_names(market_list)
df = input_base(check_list)
print(df)