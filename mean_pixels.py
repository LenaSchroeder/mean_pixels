# This is my project

RedValue = 100
RedValue2 = 50

GreenValue = 0
GreenValue2 = 100

BlueValue = 0
BlueValue2 = 0

ReadinessValue = 0
ReadinessValue2 = 200

PixelBrightness1 = (RedValue + GreenValue + BlueValue) / 3
PixelBrightness2 = (RedValue2 + GreenValue2 + BlueValue2) / 3

result_brightness3 = (PixelBrightness1 + PixelBrightness2) / 2
print(result_brightness3)

