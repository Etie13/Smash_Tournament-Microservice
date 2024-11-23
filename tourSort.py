# Author: Eric Etie
# Last Modified: 11/10/2024
# Course: CS 361
# Description: Sorts JSON objects by date that represents SmashBro tournaments

import zmq
import datetime as datetime


# Set up connection
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Receive Message
    tours = socket.recv_json()

    # pop the user filter
    filters = tours.pop()

    # Sort the tours by startDate
    sorted_tours = sorted(tours, key=lambda x: datetime.datetime.strptime(x['startDate'], "%m-%d-%Y"))

    # Initialize a new list of tours, so we can append each JSON object to match the user filter
    tours_requested = []

    # If no date filer is selected, send all tours that match the game type
    if filters['startFilter'] is None and filters['endFilter'] is None:
        if filters['gameFilter'] is None:
            socket.send_json(sorted_tours)
        else:
            for tour in sorted_tours:
                if tour['game'] == ['gameFilter'] or tour['game'] == 'both':
                    tours_requested.append(tour)

    # If there is a start date filter, but no end date filter, return the tours such that startFilter <= tour
    elif filters['startFilter'] is not None and filters['endFilter'] is None:

        # return the tours based on game type
        if filters['gameFilter'] is None:
            for tour in sorted_tours:
                if (datetime.datetime.strptime(filters['startFilter'], "%m-%d-%Y")
                        <= datetime.datetime.strptime(tour['startDate'], "%m-%d-%Y")):
                    tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'melee':
            for tour in sorted_tours:
                if tour['game'] == 'melee' or tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['startFilter'], "%m-%d-%Y")
                            <= datetime.datetime.strptime(tour['startDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'ultimate':
            for tour in sorted_tours:
                if tour['game'] == 'ultimate' or tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['startFilter'], "%m-%d-%Y")
                            <= datetime.datetime.strptime(tour['startDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'both':
            for tour in sorted_tours:
                if tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['startFilter'], "%m-%d-%Y")
                            <= datetime.datetime.strptime(tour['startDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

    # if there is a end date selected, but no start date selected, return the tours such that tour <= endFilter
    elif filters['startFilter'] is None and filters['endFilter'] is not None:

        # return the tours based on game type
        if filters['gameFilter'] is None:
            for tour in sorted_tours:
                if (datetime.datetime.strptime(filters['endFilter'], "%m-%d-%Y")
                        >= datetime.datetime.strptime(tour['endDate'], "%m-%d-%Y")):
                    tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'melee':
            for tour in sorted_tours:
                if tour['game'] == 'melee' or tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['endFilter'], "%m-%d-%Y")
                            >= datetime.datetime.strptime(tour['endDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'ultimate':
            for tour in sorted_tours:
                if tour['game'] == 'ultimate' or tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['endFilter'], "%m-%d-%Y")
                            >= datetime.datetime.strptime(tour['endDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'both':
            for tour in sorted_tours:
                if tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['endFilter'], "%m-%d-%Y")
                            >= datetime.datetime.strptime(tour['endDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

    # If there is both a start filter and end filter, return the tours such that startFilter <= tour <= endFilter
    elif filters['startFilter'] is not None and filters['endFilter'] is not None:

        # return the tours based on game type
        if filters['gameFilter'] is None:
            for tour in sorted_tours:
                if (datetime.datetime.strptime(filters['startFilter'], "%m-%d-%Y")
                        <= datetime.datetime.strptime(tour['startDate'], "%m-%d-%Y")) and (
                        datetime.datetime.strptime(filters['endFilter'], "%m-%d-%Y")
                        >= datetime.datetime.strptime(tour['endDate'], "%m-%d-%Y")):
                    tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'melee':
            for tour in sorted_tours:
                if tour['game'] == 'melee' or tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['startFilter'], "%m-%d-%Y")
                        <= datetime.datetime.strptime(tour['startDate'], "%m-%d-%Y")) and (
                            datetime.datetime.strptime(filters['endFilter'], "%m-%d-%Y")
                            >= datetime.datetime.strptime(tour['endDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'ultimate':
            for tour in sorted_tours:
                if tour['game'] == 'ultimate' or tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['startFilter'], "%m-%d-%Y")
                        <= datetime.datetime.strptime(tour['startDate'], "%m-%d-%Y")) and (
                            datetime.datetime.strptime(filters['endFilter'], "%m-%d-%Y")
                            >= datetime.datetime.strptime(tour['endDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

        elif filters['gameFilter'] == 'both':
            for tour in sorted_tours:
                if tour['game'] == 'both':
                    if (datetime.datetime.strptime(filters['startFilter'], "%m-%d-%Y")
                        <= datetime.datetime.strptime(tour['startDate'], "%m-%d-%Y")) and (
                            datetime.datetime.strptime(filters['endFilter'], "%m-%d-%Y")
                            >= datetime.datetime.strptime(tour['endDate'], "%m-%d-%Y")):
                        tours_requested.append(tour)
            socket.send_json(tours_requested)

context.destroy()
