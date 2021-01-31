# fishtank
## A fish tank controller by ESP32

学习Micropython的一个小实践

目标是做一个鱼缸景观的控制器

控制水循环、补光、加温、雾化

通过web配置运行参数

传感器： DS18B20 *2 DHT11*1
0124：
AP热点修改无线


### ESP32资源
| PIN | 模式 | 外设 |
|:---|:-----|:----|
| 2 | OUT | 指示灯 |
|4 | onewire | 18B20 |
|25| PWM | 蜂鸣器|
|22 |    | WS2812B |
|27 | onewire | DHT11|
|   |       | switch |
|   |       | switch |
|   |       | switch |
|   |       | switch |


