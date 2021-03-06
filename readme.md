Звіт команди № 3 з виконання проєкту з дискретної математики. Тема № 6. 

Завдання полягало у створенні бібліотеки для роботи з відношеннями. Виконання поставленого завдання було розбите на декілька частин. 

1) Розробка функцій read_file (читає файл та повертає матрицю в ньому як список списків), write_file (записує матрицю у файл). Під час написання цих функцій не були залучені знання з дискретної математики. 

2) Розробка функцій find_reflexive (повертає рефлексивне замикання заданої матриці), find_equal (повертає список що містить списки з елементами класів еквівалентності матриці), find_symmetric(створює матрицю, яка є симетричним замиканням), find_transitive (повертає матрицю, створену таким чином, що вона стає тразитивним замиканням заданої; для реалізації цієї функції було використано алгоритм Уоршалла), check_transitive (отримує як аргумент готову матрицю і повертає булеве значення True/False залежно від того, чи матриця транзитивна, для реалізації також використовувався алгоритм Уоршала), generate_matrix (генерує усі можливі транзитивні матриці заданого розміру (у ході виконання генерує кожен елемент один за одним та перевіряє чи не руйнує новий згенерований транзитивності вже створеної матриці для пришвидшення процесу)), count_transitive (повертає кількість усіх можливих транзитивних матриць заданого розміру).

3) Тестування програми. Виконувалось викликом усіх функцій, записом результатів їх роботи (в тому числі й часу виконання) у відповідні файли та перевіркою вручну на те чи відповідають отримані файли очікуваним. Код, який це робить знаходиться у окремих модулях test.py та test_6.py. Всі результати можна знатйти у папці after та у файлі 6_task

Процес виконання проєкту був розділений на декілька етапів:

1) Зустріч команди для вибору та обговорення теми проєкту. Ми зупинились на темі №6, адже вона видалась нам цікавою та зрозумілою у плані реалізації, до того ж, це була чудова практика з підготовки до іспиту. 

2) Розподіл завдань між учасницями команди. Кожна з нас виконувала якусь частину практичного завдання. 

Цепілова Олександра: лідерка команди, виконувала організаційну роботу та допомагала решті команди у написанні коду, написала функції count_transitive та check_transitive.
Караїм Олена: find_symmetric, тестування, test.py.
Косик Дарина: find_transitive, написання звіту, test_6.py. 
Максим'юк Юлія: read_file, find_reflexive.
Максим'юк Вікторія: write_file, find_equal.


3) Онлайн зустріч команди для обговорення результатів виконання практичної частини завдання та пояснення своїх функцій решті команди, аби кожна членкиня команди орієнтувалась у всьому коді проєкту. 

4) Тестування та аналіз результатів.

5) Написання звіту щодо реалізації проєкту, розміщення коду проєкту та звіту на платформі Github. 

Враження від виконання проєкту та фідбек викадачам та асистентам: 

Уся комада отримала задоволення від групової роботи та виконання проєкту. Нам сподобалось прикладне використання знань із дискретної математики у програмуванні. Вдячні викладачам та асистентам за надану підтримку під час усього процесу реалізації проєкту! 



