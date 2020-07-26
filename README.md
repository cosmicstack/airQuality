# airQuality
raspi project to track air quality


Sensor: SDS011
Datasheet: https://learn.watterott.com/sensors/sds011/sds011.pdf

No of bytes     Name              Content
0               Message header    AA
1               Commander No.     C0
2               DATA 1            PM2.5 Low byte
3               DATA 2            PM2.5 High byte
4               DATA 3            PM10 Low byte
5               DATA 4            PM10 High byte
6               DATA 5            ID byte 1
7               DATA 6            ID byte 2
8               Check-sum         Check-sum
9               Message tail       AB
