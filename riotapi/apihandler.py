import requests, time

def getJsonFromURL(URL, attempts, sleepTime=None):
    attempt = 0
    while attempt < attempts:
        attempt += 1

        response = requests.get(URL)
        response.connection.close()
        response = response.json()

        if 'status' in response:
            print(response)
            if sleepTime == None:
                sleepTime = attempt*2
            print('[riotapi/match] getting API response failed, retrying in %s seconds' %(sleepTime))
            time.sleep(sleepTime)
        else:
            break


    return response