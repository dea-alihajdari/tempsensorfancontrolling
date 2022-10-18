def on_button_pressed_a():
    pins.analog_write_pin(AnalogPin.P1, 1023)
    pins.analog_write_pin(AnalogPin.P12, 1023)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P12, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

fanPerctage = 0
fanSpeed = 0
tempValue = 0
maxTemp = 35
# basic.show_string("FAN SPEED: " + ("" + str(fanSpeed)))
# basic.show_string("FAN PERCTAGE: " + ("" + str(fanPerctage)))

def on_forever():
    global tempValue, fanSpeed, fanPerctage
    minTemp = 0
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P2, True, True, True)
    tempValue = dht11_dht22.read_data(dataType.TEMPERATURE)
    serial.write_value("TEMPERATURE: ", tempValue)
    # serial.write_value("Max temp: ", maxTemp)
    basic.show_string("TEMPERATURE: " + ("" + str(tempValue)))
    basic.show_string("" + str(dht11_dht22.read_data(dataType.HUMIDITY)))
    if tempValue < minTemp:
        fanSpeed = 0
        pins.analog_write_pin(AnalogPin.P0, fanSpeed)
        fanPerctage = fanSpeed * 100 / 1023
        serial.write_value("Fan SPEED: ", fanSpeed)
        serial.write_value("Fan PERCTAGE: ", fanPerctage)
        basic.show_string("FAN SPEED: " + ("" + str(fanSpeed)))
        basic.show_string("FAN PERCTAGE: " + ("" + str(fanPerctage)))
    elif tempValue >= minTemp and tempValue <= maxTemp:
        basic.show_string("FAN SPEED: " + ("" + str(fanSpeed)))
        basic.show_string("FAN PERCTAGE: " + ("" + str(fanPerctage)))
        fanSpeed = tempValue
        fanSpeed = 29.5 * fanSpeed
        fanPerctage = fanSpeed * 100 / 1023
        pins.analog_write_pin(AnalogPin.P0, fanSpeed)
        serial.write_value("Fan SPEED: ", fanSpeed)
        serial.write_value("Fan PERCTAGE: ", fanPerctage)
        basic.show_string("FAN SPEED: " + ("" + str(fanSpeed)))
        basic.show_string("FAN PERCTAGE: " + ("" + str(fanPerctage)))
    elif tempValue > maxTemp:
        fanSpeed = 1023
        fanPerctage = fanSpeed * 100 / 1023
        pins.analog_write_pin(AnalogPin.P0, fanSpeed)
        serial.write_value("Fan SPEED: ", fanSpeed)
        serial.write_value("Fan PERCTAGE: ", fanPerctage)
        basic.show_string("FAN SPEED: " + ("" + str(fanSpeed)))
        basic.show_string("FAN PERCTAGE: " + ("" + str(fanPerctage)))
basic.forever(on_forever)
