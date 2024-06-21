class Task:
    # Конструктор класса Task, инициализирует описание, срок и статус выполнения
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False  # По умолчанию задача не выполнена

    # Метод для отметки задачи как выполненной
    def mark_as_completed(self):
        self.completed = True

    # Метод для текстового представления задачи
    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Описание: {self.description}, Срок: {self.due_date}, Статус: {status}"

class TaskManager:
    # Конструктор класса TaskManager, инициализирует пустой список задач
    def __init__(self):
        self.tasks = []

    # Метод для добавления новой задачи в список
    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    # Метод для отметки задачи как выполненной по индексу
    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Неверный индекс задачи")

    # Метод для получения списка текущих (не выполненных) задач
    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        return current_tasks

    # Метод для вывода всех задач
    def display_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"Задача {i}: {task}")

    # Метод для вывода текущих (не выполненных) задач
    def display_current_tasks(self):
        current_tasks = self.get_current_tasks()
        if not current_tasks:
            print("Нет текущих (не выполненных) задач")
        else:
            for i, task in enumerate(current_tasks, 1):
                print(f"Текущая задача {i}: {task}")

# Создание экземпляра TaskManager
task_manager = TaskManager()

# Добавление задач
task_manager.add_task("Купить продукты", "2024-06-22")
task_manager.add_task("Подготовить отчет", "2024-06-25")

# Вывод всех задач
print("Все задачи:")
task_manager.display_tasks()

# Отметка первой задачи как выполненной
task_manager.mark_task_completed(0)

# Вывод всех задач
print("Все задачи:")
task_manager.display_tasks()

# Вывод текущих (не выполненных) задач
print("\nТекущие задачи:")
task_manager.display_current_tasks()
