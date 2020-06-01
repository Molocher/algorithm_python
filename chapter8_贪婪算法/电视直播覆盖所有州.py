# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 16:36
# @Author  : Molo.Qu


state_needed = set(['mt','wa','or','id','nv','ut','ca','az'])
stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthress'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])

final_stations = set()

while state_needed:
    best_stations =None
    states_covered = set()
    for station,states_for_station in stations.items():
        coverd = state_needed & states_for_station
        if len(coverd) > len(states_covered):
            best_stations = station
            states_covered = coverd
    final_stations.add(best_stations)
    state_needed -= states_covered

print(final_stations)
