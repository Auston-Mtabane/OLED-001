from machine import Pin, I2C
import ssd1306
import time

# --- Configure I2C with new pins ---
i2c = I2C(0, scl=Pin(22), sda=Pin(4))  # SCL=22, SDA=4

# --- Initialize OLED ---
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# --- Clear screen ---
oled.fill(0)
oled.show()

# --- Display text ---
oled.text("Hello ESP32!", 0, 0)
oled.text("Using GPIO4 SDA", 0, 10)
oled.show()
time.sleep(2)

oled.fill(0)
oled.show()

# --- Simple animation ---
for i in range(0, 64, 8):
    oled.fill_rect(0, i, 128, 4, 1)
    oled.show()
    time.sleep(0.1)

