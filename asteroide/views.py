from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view!')

def profile(request):
    jsonList = []
    req = requests.get('https://api.github.com/users/DrkSephy')
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonList:
        userData['name'] = data['name']
        userData['blog'] = data['blog']
        userData['email'] = data['email']
        userData['public_gists'] = data['public_gists']
        userData['public_repos'] = data['public_repos']
        userData['avatar_url'] = data['avatar_url']
        userData['followers'] = data['followers']
        userData['following'] = data['following']
    parsedData.append(userData)
    #return HttpResponse(parsedData)
    return render(request,'asteroide/profile.html', {'data': parsedData})

def infoasteroid (request):
    jsonList = []
    req = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=yRWllVz2NGf8KMs6L1y1YlLM13rbRCD3TB62SHvO')
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    #print jsonList[0]
    for fecha in jsonList[0]['near_earth_objects']:
        # print jsonList[0]['near_earth_objects'][data]
        for asteroidDictN in range (0,len(jsonList[0]['near_earth_objects'][fecha])):
            userData[jsonList[0]['near_earth_objects'][fecha][asteroidDictN]['name']]={}
            userData[jsonList[0]['near_earth_objects'][fecha][asteroidDictN]['name']]["neo_reference_id"] = jsonList[0]['near_earth_objects'][fecha][asteroidDictN]["neo_reference_id"]
            userData[jsonList[0]['near_earth_objects'][fecha][asteroidDictN]['name']]["nasa_jpl_url"] = jsonList[0]['near_earth_objects'][fecha][asteroidDictN]["nasa_jpl_url"]
            userData[jsonList[0]['near_earth_objects'][fecha][asteroidDictN]['name']]["absolute_magnitude_h"] = jsonList[0]['near_earth_objects'][fecha][asteroidDictN]["absolute_magnitude_h"]
            userData[jsonList[0]['near_earth_objects'][fecha][asteroidDictN]['name']]["is_potentially_hazardous_asteroid"] = jsonList[0]['near_earth_objects'][fecha][asteroidDictN]["is_potentially_hazardous_asteroid"]
            userData[jsonList[0]['near_earth_objects'][fecha][asteroidDictN]['name']]["estimated_diameter"] = jsonList[0]['near_earth_objects'][fecha][asteroidDictN]["estimated_diameter"]
            print userData[jsonList[0]['near_earth_objects'][fecha][asteroidDictN]['name']]
        # userData['blog'] = jsonList[0][data]['2015-09-08'][0]['name']
        # userData['email'] = jsonList[0][data]['2015-09-08'][0]['name']
        # userData['public_gists'] = jsonList[0][data]['2015-09-08'][0]['name']
        # userData['public_repos'] = jsonList[0][data]['2015-09-08'][0]['name']
        # userData['avatar_url'] = jsonList[0][data]['2015-09-08'][0]['name']
        # userData['followers'] = jsonList[0][data]['2015-09-08'][0]['name']
        # userData['following'] = jsonList[0][data]['2015-09-08'][0]['name']
        parsedData.append(userData)
    #return HttpResponse(parsedData)
    return render(request,'asteroide/infoasteroid.html', {'data': userData})
