#  read in some environment variables from the Balena cloud

### https://docs.balena.io/reference/balena-cli/#envs
balena envs shows that both fleet and device parameters have been set via balena-cloud
```
val@pop-os:~/balenaFiles/minBalenaPisound/Balena-env-python$ balena envs --fleet val-one
ID     NAME VALUE                      FLEET          SERVICE
786437 foo  "this is foo - fleet wide" vveirs/val-one *
```
## ## getvars.py demonstrates getting fleet and device parameter values from balena-cloud
```
val@pop-os:~/balenaFiles/minBalenaPisound/Balena-env-python$ balena envs --device c07e57f4fba0c2d2a699a9f75eae0f24
ID[getvars.py](getvars.py)       NAME VALUE                       FLEET          DEVICE                           SERVICE
15581791 bar  "this is bar -- one device" vveirs/val-one c07e57f4fba0c2d2a699a9f75eae0f24 *
786437   foo  "this is foo - fleet wide"  vveirs/val-one *                                *
```

## Now, let's look into accessing these variables from python
###https://github.com/balena-io/balena-fleet-management-masterclass

REMEMBER, set API_TOKEN=your_api_token in each new instance of a terminal

```
 balena devices --fleet val-one
ID       UUID    DEVICE NAME DEVICE TYPE     FLEET          STATUS IS ONLINE SUPERVISOR VERSION OS VERSION            DASHBOARD URL
12415605 c07e57f white-surf  raspberrypi4-64 vveirs/val-one Idle   true      14.11.2            balenaOS 2.115.7+rev1 https://dashboard.balena-cloud.com/devices/c07e57f4fba0c2d2a699a9f75eae0f24/summary

get device identifier
curl -X POST 'https://api.balena-cloud.com/v5/device_config_variable' -H "Authorization: Bearer $API_TOKEN" -H 'Content-Type: application/json' -d '{
    "device": "c07e57f",
    "name": "RESIN_SUPERVISOR_PERSISTENT_LOGGING",
    "value": "1"
}'

curl -X GET 'https://api.balena-cloud.com/v5/application?$filter=app_name%20eq%20%27val-one%27' -H "Authorization: Bearer $API_TOKEN" -H 'Content-Type: application/json' | jq '.'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   386  100   386    0     0   1129      0 --:--:-- --:--:-- --:--:--  1128
{
  "d": [
    {
      "id": 2054214,
      "user": {
        "__id": 132052
      },
      "actor": 15962006,
      "app_name": "val-one",
      "slug": "vveirs/val-one",
      "commit": "d53f0f168a8b180d0eb6d97bf8dcba3b",
      "application_type": {
        "__id": 4
      },
      "device_type": "raspberrypi4-64",
      "should_track_latest_release": true,
      "is_accessible_by_support_until__date": null,
      "is_public": false,
      "is_host": false,
      "is_archived": false,
      "created_at": "2023-05-21T19:25:31.912Z"
    }
  ]
}

curl -X POST 'https://api.balena-cloud.com/v5/device_config_variable' -H "Authorization: Bearer $API_TOKEN" -H 'Content-Type: application/json' -d '{
    "device": "12415605",
    "name": "RESIN_SUPERVISOR_PERSISTENT_LOGGING",
    "value": "1"
}'
{"id":7682693,"device":{"__id":12415605},"value":"1","name":"RESIN_SUPERVISOR_PERSISTENT_LOGGING"}


 curl -X GET 'https://api.balena-cloud.com/v5/device_config_variable?$filter=device%20eq%2012415605' -H "Authorization: Bearer $API_TOKEN" -H 'Content-Type: application/json' | jq '.'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   979  100   979    0     0   2885      0 --:--:-- --:--:-- --:--:--  2879
{
  "d": [
    {
      "id": 7542071,
      "device": {
        "__id": 12415605
      },
      "value": "1",
      "name": "RESIN_HOST_CONFIG_avoid_warnings"
    },
    {
      "id": 7542070,
      "device": {
        "__id": 12415605
      },
      "value": "1",
      "name": "RESIN_HOST_CONFIG_disable_splash"
    },
    {
      "id": 7542068,
      "device": {
        "__id": 12415605
      },
      "value": "\"vc4-kms-v3d\"",
      "name": "RESIN_HOST_CONFIG_dtoverlay"
    },
    {
      "id": 7542069,
      "device": {
        "__id": 12415605
      },
      "value": "\"i2c_arm=on\",\"spi=on\",\"audio=on\"",
      "name": "RESIN_HOST_CONFIG_dtparam"
    },
    {
      "id": 7542067,
      "device": {
        "__id": 12415605
      },
      "value": "0",
      "name": "RESIN_HOST_CONFIG_enable_uart"
    },
    {
      "id": 7542066,
      "device": {
        "__id": 12415605
      },
      "value": "16",
      "name": "RESIN_HOST_CONFIG_gpu_mem"
    },
    {
      "id": 7542065,
      "device": {
        "__id": 12415605
      },
      "value": "",
      "name": "RESIN_HOST_FIREWALL_MODE"
    },
    {
      "id": 7542063,
      "device": {
        "__id": 12415605
      },
      "value": "1",
      "name": "RESIN_SUPERVISOR_DELTA"
    },
    {
      "id": 7542064,
      "device": {
        "__id": 12415605
      },
      "value": "3",
      "name": "RESIN_SUPERVISOR_DELTA_VERSION"
    },
    {
      "id": 7682693,
      "device": {
        "__id": 12415605
      },
      "value": "1",
      "name": "RESIN_SUPERVISOR_PERSISTENT_LOGGING"
    }
  ]
}

### https://docs.balena.io/reference/sdk/python-sdk/

```

##  main  in .env file, foo equals 1.234
##  main  bar equals this is text
