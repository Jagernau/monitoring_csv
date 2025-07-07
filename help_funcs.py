
def find_child_group(data, group_id):
    """
    Ищет самую глубокую группу вложенных групп
    принимает на вход список групп и идентификатор группы
    возвращает самую глубокую группу или None, если такая группа не найден
    """

    # Ищем дочерние группы
    children = [group for group in data if group['parentId'] == group_id]
    
    if not children:
        return None  # Если дочерних групп нет, возвращаем None
    
    # Рекурсивно ищем самую дочернюю группу
    deepest_child = None
    for child in children:
        result = find_child_group(data, child['id'])
        if result is None:
            deepest_child = child  # Если у дочерней группы нет детей, она самая глубокая
        else:
            deepest_child = result  # Если есть дочерние группы, продолжаем искать
    
    return deepest_child

