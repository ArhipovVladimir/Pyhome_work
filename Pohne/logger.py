def pohne_logger(data):
    with open('pohne.cvs', 'a') as file:
        file.write('name;{}last_mame;{};pohne;{}\n'
                    .format(data[0], data[1], data[2]))


# def pressure_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log.cvs', 'a') as file:
#         file.write('{};pressure;{}\n'
#                    .format(time, data))
#
#
# def wind_speed_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log.cvs', 'a') as file:
#         file.write('{};wind_speed;{}\n'
#                    .format(time, data))
