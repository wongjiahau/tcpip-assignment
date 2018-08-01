# tcpip-assignment
## How to initialize database?

```
cd part-A
rm stationsdb.sqlite
python3.6 db.py
```

## How to test API?
### Retrieve stations (GET)
```
curl http://localhost:5000/api/stations
```

### Retrieve specific stations (GET)
```
curl http://localhost:5000/api/stations/2
```

### Create stations (POST)
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"code":"new_code","name":"my_station", "type": "newType"}' \
    http://localhost:5000/api/stations
```

### Update stations (PUT)
```
curl --header "Content-Type: application/json" \
    --request PUT \
    --data '{"code":"upd_code","name":"upd_station", "type": "upd_type", "id": 1}' \
    http://localhost:5000/api/stations/1
```

### Delete stations (DELETE)
```
curl --header "Content-Type: application/json" \
    --request DELETE \
    --data '{"id": 1}' \
    http://localhost:5000/api/stations/1
```
