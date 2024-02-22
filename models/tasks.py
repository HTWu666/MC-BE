from utils.search import binary_search
from exceptions.tasks import TaskNotFoundException


class Task:
    # mock the table/collection in database
    tasks_list = []
    last_task_id = 0  # for auto increment

    @classmethod
    def get_all(cls):
        return cls.tasks_list

    @classmethod
    def create(cls, name, status=False):
        # insert a new task into tasks list
        cls.last_task_id += 1  # id is auto increment
        task = {"id": cls.last_task_id, "name": name, "status": status}
        cls.tasks_list.append(task)

        return task

    @classmethod
    def update(cls, task_id, name, status):
        # find the match task
        task_index = binary_search(cls.tasks_list, task_id)
        if task_index == -1:
            raise TaskNotFoundException(f"Task with ID {task_id} does not exist.")

        # update the match task
        cls.tasks_list[task_index]["name"] = name
        cls.tasks_list[task_index]["status"] = status

        return {"id": task_id, "name": name, "status": status}

    @classmethod
    def delete(cls, task_id):
        # find the match task
        task_index = binary_search(cls.tasks_list, task_id)
        if task_index == -1:
            raise TaskNotFoundException(f"Task with ID {task_id} does not exist.")

        # delete the match task
        del cls.tasks_list[task_index]

        return True
