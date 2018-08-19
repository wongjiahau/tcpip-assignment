# tcpip-assignment
## How to initialized database?

```sh
cd part-A
rm stationsdb.sqlite
python3.6 db.py
```

## How to test API?
### 1. Retrieve stations (GET)
```sh
curl http://localhost:5000/api/stations
```

### 2. Retrieve specific stations (GET)
```sh
curl http://localhost:5000/api/stations/2
```

### 3. Create stations (POST)
```sh
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"code":"new_code","name":"my_station", "type": "newType"}' \
    http://localhost:5000/api/stations
```

### 4. Update stations (PUT)
```sh
curl --header "Content-Type: application/json" \
    --request PUT \
    --data '{"code":"SBK08","name":"upd_station", "type": "upd_type"}' \
    http://localhost:5000/api/stations/SBK08
```

### 5. Delete stations (DELETE)
```
curl --header "Content-Type: application/json" \
    --request DELETE \
    --data '{"id": 1}' \
    http://localhost:5000/api/stations/1
```