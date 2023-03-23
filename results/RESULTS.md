# Пояснювальна записка та висновок до лабораторного практикуму

Результатом лабораторного практикуму для 3 країн

1. Іспанія
2. Бангладеш
3. Ісландія

є наступні матеріали.

## Кодова база

### Python code

- [unzipping_files.py](src/unzipping_files.py)

### Jupiter Notebooks

- [graphs_with_results.ipynb](src/graphs_with_results.ipynb)


### Файли

#### Вхідні дані (разархівовані та сконвертовані дані)

##### Oil Prices

- CSV: [brent-year](data/oil-prices-master/data/brent-year.csv)
- JSON: [brent-year](data/oil-prices-master/data/brent-year.json)
- XLSX: [brent-year](data/oil-prices-master/data/brent-year.xlsx)

##### Wti

- CSV: [wti-year](data/oil-prices-master/data/wti-year.csv)
- JSON: [wti-year](data/oil-prices-master/data/wti-year.json)
- XLSX [wti-year](data/oil-prices-master/data/wti-year.xlsx)

##### Population

- CSV: [population](data/population-master/data/population.csv)
- JSON: [population](data/population-master/data/population.json)
- XLSX [population](data/population-master/data/population.xlsx)

##### Purchasing power parity (PPP)

- CSV: [ppp](data/ppp-master/data/ppp-gdp.csv)
- JSON: [ppp](data/ppp-master/data/ppp-gdp.json)
- XLSX [ppp](data/ppp-master/data/ppp-gdp.xlsx)


---

## Інструкція до роботи

1. Запускаемо [unzipping_files.py](src/unzipping_files.py).
2. Результат программи 1:
    1. Дістаємо дані з архівів
    2. Зчитуємо дані та змінюємо формат дати для подальшої роботи
    3. Зберігаємо дані в 3-х форматах (сsv, xlsx, json)
3. Виконуємо код програми 2 в ноутбук [graphs_with_results.ipynb](src/graphs_with_results.ipynb)
4. Результат программи 2
    1. Популяція за 1960-2018 роки: [лінійний графік](img/population_countries_line.png), [кругова діаграма](img/population_countries_pie.png), [стовпчаста діаграма](img/population_countries_bar.png)
    2. Основні статистичні показники чисельності населення країн: [Іспанія](img/main_statistical_values_spain.png), [Бангладеш](img/main_statistical_values_bangladesh.png), [Ісландія](img/main_statistical_values_iceland.png)
    3. Зв'язок між цінами на нафту та паритетом купівельної спроможності: [графік](img/correlation_oil_ppp.png)
    4. Зв'язок між населенням та паритетом купівельної спроможності: [графік](img/correlation_population_ppp.png)
    5. Зв'язок між цінами на нафту та населенням: [графік](img/correlation_population_oil.png)
    6. Відсоток паритету купівельної спроможності окремої країни до середнього показника паритету купівельної спроможності усіх країн: [графік](img/percentage_ppp.png)
