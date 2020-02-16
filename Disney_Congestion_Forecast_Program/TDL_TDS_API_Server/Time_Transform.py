import datetime
def Time_Transform(data,dict):
    output_date = datetime.datetime.strptime(data['operatings'][0][dict], "%Y-%m-%dT%H:%M:%S.%fZ") + datetime.timedelta(hours=9)
    return output_date.strftime("%H:%M")

if __name__ == "__main__":
    pass