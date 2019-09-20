# Задачи

## 1. Вводная лекция

### 1. Основы git и bash

1. Упражения с git на новом репозитории

- Создать локальный пустой репозиторий
- Добавить файл, сделать коммит.
- Откатиться туда и обратно.

2. Упражнения с git на готовом репозитории

- Сделать форк основного репозитория
- Вытянуть локально репозиторий
- Добавить пустой файл

### 2. Основы Python

1. Рукопожатие — один из способов приветсвия, который нам достался из античности. Студенты Политеха тоже здоровоются рукопожатием. Обычно парни. Сколько раз жмут руку друг другу парни при встрече, если каждый здоровается с каждым?  Напишите функцию, которая вычисляет это значение.
2. На чемпионате The Internetional  в следующем году будет учавствовать много команд. Сколько существует вариантов распределить первые три места? А все места? Напишите функцию, которая вычисляет эти значения.
3. Вы разработчик в компании, которая выполняет заказ для государственной раздведовательной службы. Сейчас Ваш отдел работает над анализом соиологических данных по одной бедной азиатской стране. Недавно там приняли новую программу поддержки рождаемости. Правильство дает за рождение мальчика огромную сумму денег. Но больше одного мальчика иметь нельзя. При этом количество детей в семье неограниченно. Руководство попросило Вас составить прогноз и понять какое будет распределение мужчин и женщин в этой азиатской стране в будущем, если каждая семья будет рожать до тех пор, пока не родится мальчик. Модель должна быть простой. Напишите программу, которая моделирует рождаемость в этой стране. Можно ли решить задачу аналитически?
4. Вы разработчик игр и разбираетсь с жалобами игроков. Многие ругаются, что герои часто застревают в текстурах. Оказалось, что функция, которая проверяет пересечение фигуры героя со стенами написана с ошибкой. Надо переписать. Напишите функцию, которая проверяет пересекаются ли два прямоугольника. Они заданы двумя точками диагонали, стороны параллельны осям декартовой системы координат. Можно ли переписать программу так, чтобы она выдавала координаты пересечения?
5. Вы разработчик игр и работаете над новой фичей (функцией) для игры. Сейчас надо реализовать логику работы сражений в игре. Во время сражения игрока с противником каждый наносит удар. У кого сила удара больше, тот и нанес урон. Противники в игре — боты. За них никто не играет. Поэтому силу удара надо формировать случайно. Напишите функцию, которая выдает псевдослуайное число силы удара. Сделайте это с помощью  линейного конгруэнтного метода <img src="https://render.githubusercontent.com/render/math?math=x_{n%2B1} =(a x_n%2Bc)\mod m">, где <img src="https://render.githubusercontent.com/render/math?math=x_0&mode=inline"> — seed.

5. Вы разработчик программ для банка. Руководство попросило Вас написать программу для печати квитанций и чеков. На чеках надо рядом с суммой выводить ее значение текстом. Это нужно, чтобы сложнее было подделать бумаги. Одну цифру легко исправить, а если еще и слово переписать, то сложнее. Напишите программу, которая выводит текстовую строку для целого числа.
6. Вы автор программы №1.2.2. Вашу программу захотела купить компания 1xbet, чтобы анализировать ставки. Но они хотят, чтобы программа работала быстрее с большими числами. Можно ли ускорить программу? Математики из компании утверждают, что можно использовать для этого разложение на простые множители.
7. Вы разработчик игр и ваш коллега написал только что функцию проверки на пересечение двух прямоугольников, которые заданы двумя точками диагонали. Надо проверить не сделал ли он ошибок. Напишите проверки. Для этого используйте конструкцию `assert`.
8. Вы разработчик игр и работаете над новой фичей (функцией) для игры. Сейчас надо реализовать логику работы сражений в игре. Во время сражения игрока с противником каждый наносит удар. У кого сила удара больше, тот и нанес урон. Напишите функцию, которая реализует эту логику. К сожалению, игра для старой слабой платформы, где нет аппаратной поддержки операций сравнения. Поэтому надо написать код без них. Разработчики аппаратуры подсказали, что можно использовать бинарное представление чисел.

## 2. Алгоритмы и структуры данных. Начало

### 1. Алгоритмы поиска

1. В системе регистрации сайта был сбой и в списке идентификаторов пользователей есть повторяющиеся идентификаторы. Напишите программу, которая проверяет есть ли повторовы. Попробуйте найти решение за квазилинейное время.
2. Случаи ошибок участились, руководство просит ускорить систему поиска повторов из задачи №2.1.1. Попробуйте ускорить
алгоритм до линейного времени.