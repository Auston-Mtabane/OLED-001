# ESP32 MicroPython OLED Project

This project demonstrates how to use a **128x64 I²C OLED display** with an **ESP32** running **MicroPython**. You can display text, draw pixels, rectangles, lines, and simple animations on the OLED.

---

## 📦 Hardware Requirements

* ESP32 (DOIT WROOM or similar)
* 128x64 I²C OLED display (SSD1306)
* Jumper wires
* Optional: Breadboard

**Default pin configuration for this project:**

| OLED Pin | ESP32 Pin |
| -------- | --------- |
| VCC      | 3.3V      |
| GND      | GND       |
| SDA      | GPIO4     |
| SCL      | GPIO22    |

---

## ⚡ Software Requirements

* [MicroPython firmware for ESP32](https://micropython.org/download/esp32/)
* [Thonny IDE](https://thonny.org/) or another editor with MicroPython support
* `ssd1306.py` MicroPython driver (included in this project)

---

## 📝 Installation Steps

### 1. Flash MicroPython onto ESP32

1. Download MicroPython `.bin` for ESP32.
2. Connect your ESP32 to PC.
3. Use `esptool.py` to flash:

```bash
esptool.py --chip esp32 --port COMx erase_flash
esptool.py --chip esp32 --port COMx --baud 460800 write_flash -z 0x1000 esp32-xxxx.bin
```

Replace `COMx` with your port and `.bin` with downloaded firmware.

---

### 2. Upload SSD1306 driver to ESP32

1. Open **Thonny IDE**.
2. Open the `ssd1306.py` file included in this repository.
3. **File → Save as → MicroPython device**.
4. This will copy the driver into ESP32 flash memory.

---

### 3. Upload example script

1. Open `oled_example.py` (or your main Python script).
2. Check that the I²C pins match your wiring:

```python
from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(22), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
```

3. **Run** the script in Thonny.
4. The OLED should display text and shapes.

---

## 🔹 Optional: Auto-run on boot

To make the program run automatically on power-up:

1. Save your main script as `main.py`
2. Upload it to **MicroPython device** via Thonny.

ESP32 will execute it every time it starts.

---

## 🖌️ Drawing Functions

Use the following methods for graphics:

```python
oled.fill(0)                   # Clear screen
oled.text("Hello!", 0, 0)      # Display text
oled.pixel(x, y, 1)            # Draw pixel
oled.framebuf.fill_rect(x, y, w, h, 1)  # Draw filled rectangle
oled.show()                     # Update OLED
```

---

## ⚡ Troubleshooting

* **No display detected:**

  * Check wiring (SDA/SCL, VCC, GND)
  * Make sure I²C pins in code match physical pins
  * Try lowering I²C frequency: `I2C(0, scl=Pin(22), sda=Pin(4), freq=100000)`

* **Random pixels / blinking:**

  * Check voltage (3.3V recommended)
  * Ensure good connections

---

## 🧰 References

* [MicroPython official docs](https://docs.micropython.org/)
* [SSD1306 MicroPython driver](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py)
