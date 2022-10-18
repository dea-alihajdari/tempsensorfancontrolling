input.onButtonPressed(Button.A, function () {
    pins.analogWritePin(AnalogPin.P1, 1023)
    pins.analogWritePin(AnalogPin.P12, 1023)
})
input.onButtonPressed(Button.B, function () {
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P12, 0)
})
let fanPerctage = 0
let fanSpeed = 0
let tempValue = 0
let maxTemp = 35
// basic.show_string("FAN SPEED: " + ("" + str(fanSpeed)))
// basic.show_string("FAN PERCTAGE: " + ("" + str(fanPerctage)))
basic.forever(function () {
    let minTemp = 0
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P2,
    true,
    true,
    true
    )
    tempValue = dht11_dht22.readData(dataType.temperature)
    serial.writeValue("TEMPERATURE: ", tempValue)
    // serial.write_value("Max temp: ", maxTemp)
    basic.showString("TEMPERATURE: " + tempValue)
    basic.showString("" + dht11_dht22.readData(dataType.humidity))
    if (tempValue < minTemp) {
        fanSpeed = 0
        pins.analogWritePin(AnalogPin.P0, fanSpeed)
        fanPerctage = fanSpeed * 100 / 1023
        serial.writeValue("Fan SPEED: ", fanSpeed)
        serial.writeValue("Fan PERCTAGE: ", fanPerctage)
        basic.showString("FAN SPEED: " + fanSpeed)
        basic.showString("FAN PERCTAGE: " + fanPerctage)
    } else if (tempValue >= minTemp && tempValue <= maxTemp) {
        basic.showString("FAN SPEED: " + fanSpeed)
        basic.showString("FAN PERCTAGE: " + fanPerctage)
        fanSpeed = tempValue
        fanSpeed = 29.5 * fanSpeed
        fanPerctage = fanSpeed * 100 / 1023
        pins.analogWritePin(AnalogPin.P0, fanSpeed)
        serial.writeValue("Fan SPEED: ", fanSpeed)
        serial.writeValue("Fan PERCTAGE: ", fanPerctage)
        basic.showString("FAN SPEED: " + fanSpeed)
        basic.showString("FAN PERCTAGE: " + fanPerctage)
    } else if (tempValue > maxTemp) {
        fanSpeed = 1023
        fanPerctage = fanSpeed * 100 / 1023
        pins.analogWritePin(AnalogPin.P0, fanSpeed)
        serial.writeValue("Fan SPEED: ", fanSpeed)
        serial.writeValue("Fan PERCTAGE: ", fanPerctage)
        basic.showString("FAN SPEED: " + fanSpeed)
        basic.showString("FAN PERCTAGE: " + fanPerctage)
    }
})
