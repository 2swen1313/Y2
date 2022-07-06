from itertools import permutations

"""point_list = [A_post_office, B_griboedova, C_beiker, D_bol_sadovaya, E_green_alley]"""
point_list = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
route_list = list(permutations(point_list[1:]))  # список возможных маршрутов
postman_dict = {}  # карта почтальена в виде словаря


def distance_beetwen_two_points(a, b):  # формула расссчета расстояния между двумя точами
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


for route in route_list:  # для каждого маршрута из списка возможных маршрутов

    distance_list = []  # список расстояний

    for i in range(len(route) - 1):  # для каждого отрезка пути в путях в каждом маршруте

        distance_list.append(distance_beetwen_two_points(route[i], route[
            i + 1]))  # список расстояний это список расстояний между отрезками пути в маршрутах

    postman_route = [point_list[0]] + list(route) + [point_list[0]]
    # список возможных маршрутов почтальена - список состоящий из это точка А, списока маршрутов и точки А опять

    postman_distance = [distance_beetwen_two_points(point_list[0], route[0])] + distance_list + [
        distance_beetwen_two_points(route[-1], point_list[0])]
    # список расстояний почтальена - это список состоящий из расстояний между точкой А и точкой из маршрута1, списка расстояний и
    # расстояния между точкой из последнего маршрута и точкой А

    postman_dict[sum(postman_distance)] = {'postman_route': postman_route, 'postman_distance': postman_distance}
    # словарь почтальена - это словарь в котором ключи это конечные расстояния маршрутов,
    # а значения 2 словаря( маршрутов и расстояний)

min_key = sorted(postman_dict)[0]  # минимальное конечное расстояние маршрута
min_value = postman_dict[min_key]  # минимальный маршрут

result = f"{min_value['postman_route'][0]}"

for i in range(len(min_value['postman_route']) - 1):
    result += f" -> {min_value['postman_route'][i + 1]}[{min_value['postman_route'][i]}]"
result += f" = {min_key}"

print(result)

