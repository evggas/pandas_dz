import pandas as pd

df = pd.read_csv("dz.csv")
print (df)

df.fillna(0, inplace=True)
print(df)

group = df.groupby('City')['Salary'].mean().reset_index()
group.columns = ['City', 'Average_Salary']  # Переименуем колонки для ясности
print("\nСредняя зарплата по городам:")
print(group)

merged_df = df.merge(group, on='City', how='left')
print("\nОбъединенные данные:")
print(merged_df)

if "Average_Salary" in merged_df.columns:
    print("\n Средняя зарплата добавлена")
else:
    print("\nОшибка добавления средней зп")
merged_df.to_csv("lessondz.csv", index=False)
print("\nРезультат сохранен в 'lessondz.csv'.")


#df.to_csv("lessondz.csv", index=False)

#group_reset = group.reset_index()
#print("\nГруппа с сброшенным индексом:")
#print(group_reset)

# Сохранение результата в новый CSV файл
#group_reset.to_csv("lessondz.csv", index=False)
#print("\nРезультат сохранен в 'lessondz.csv'.")

