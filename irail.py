#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

import urllib2
import json
import arrow
import bottle

# full station ID list here : https://github.com/iRail/stations/blob/master/stations.csv
departureID = "008814209" # Nivelles
destinationIDs = ("008886009", "008863545") # Ath & Yvoir

def getConnections() :
    connections = []
    for destinationID in destinationIDs :
        data = urllib2.urlopen("https://api.irail.be/connections/?from=%s&to=%s&format=json" % (departureID, destinationID))
        jsonList = json.loads(data.read())
        connections.extend(jsonList["connection"][0:3])
    connections.sort(key = lambda connection : connection["departure"]["time"])
    return connections

def extractConnectionData(connection) :
    destinationStationName = connection["arrival"]["stationinfo"]["name"]

    durationSeconds = int(connection["duration"])
    hours, minutes = durationSeconds / 3600, (durationSeconds % 3600) / 60
    durationString = "%02d:%02d" % (hours, minutes)

    delayMinutes = int(connection["departure"]["delay"]) / 60
    
    departureTimestamp = connection["departure"]["time"]
    departureTimeString = arrow.get(departureTimestamp).to("Europe/Brussels").format("HH:mm")
    
    return {
        "destinationStationName" : destinationStationName,
        "durationString" : durationString,
        "delayMinutes" : delayMinutes,
        "departureTimeString" : departureTimeString
        }

@bottle.route('/')
def upcomingTrains():
    connectionsJSON = getConnections()
    connectionsExtracted = [extractConnectionData(connection) for connection in connectionsJSON]
    # bottle converts the dict into JSON and adds the "application/json" accept header.
    return dict(data=connectionsExtracted)

bottle.run(host='localhost', port=8090)
