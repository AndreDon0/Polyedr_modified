# Изображение проекции полиэдра

Построение изображения полиэдра с удалением невидимых линий — пример
классической задачи, для успешного решения которой необходимо знакомство
с основами вычислительной геометрии.

![Шахматный король](images/king.png)

## Задача

Все рёбра делятся на три класса: полностью видимые, видимые частично и полностью невидимые.
Модифицируйте эталонный проект таким образом, чтобы определялась и печаталась следующая
характеристика полиэдра: сумма длин проекций полностью видимых рёбер, образующих с вертикалью угол
не более 10 градусов, проекция центра которых находится строго внутри окружности x^2+y^2=4.
*Коэффициент гомотетии и углы Эйлера влияют на изображение проекции полиэдра, но не изменяют сам полиэдр.*

Задача решалась только для `shadow` и `opyimize_7`

#### Список изменений в файле [CHANGELOG](CHANGELOG.md)!

## Проверка соблюдения соглашений о стиле программного кода

~~~{.sh}
find . -name '*.py' -exec pycodestyle {} \;
~~~

## Проверка покрытия тестами кода программы

~~~{.sh}
python -B -m coverage run -m unittest discover tests && coverage report -m ; rm -f .coverage
~~~

