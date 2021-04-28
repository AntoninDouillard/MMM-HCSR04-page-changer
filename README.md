# MMM-HCSR04-page-changer

A module for magic mirror that uses an HCSR04 sensor to enable switching between pages.

This repo is a fork of [zerosamski/MMM-Page-Pusher](https://github.com/zerosamski/MMM-Page-Pusher).
The difference between MMM-Page-Pusher and MMM-HCSR04-page-changer is MMM-HCSR04-page-changer use
only one HCSR04 instead of two.

Current development status : WIP.

Please contact me at antonin.info@protonmail.com for any issue or question.

### How it works

Node helper gets the data from the sensor every second via a python script. When you 'push' towards
the sensor it sends a socket notification to [MMM-Pages](https://github.com/edward-shen/MMM-pages).

### MagicMirror² Example Configuration

To use this module, add the following configuration block to the modules array in the config/config.js file:

```js
var config = {
    modules: [
        ...
        {
            module: "MMM-HCSR04-page-changer",
            config: {
                PinTrigger: 20, 
                PinEcho: 21, 
                debug: false, 
                threshold: 20,
                pirSensor: false,
            }
        },
        ...
    ]
}
```

### Configuration options

| Option             | Type               | Default Value            | Description                                    |
| ------------------ | ------------------ | ------------------------ | ---------------------------------------------- |
| `PinTrigger`       | `int`              | `20`                     | GPIO pin location of the trigger of the sensor |
| `PinEcho`          | `int`              | `21`                     | GPIO pin location of the echo of the sensor    |
| `debug`.           | `boolean`          | `false`                  | Enables extra loggin feature (distance measured by sensor) |
| `threshold`        | `int`              | `20`                     | Distance at which a push should be registered. Default is 20 cm, so if your hand is closer than 20 cm to the sensor, it will register it as a 'push' |
| `pirSensor`        | `boolean`          | `false`                  | If you are using MMM-PIR-Sensor with MMM-PIR-Sensor (https://github.com/paviro/MMM-PIR-Sensor) this will pause stop the script when your display is off and start it again if motion is detected and the screen is turned back on. Saves energy :) |

### Thank you

I got the idea from [MMM-Page-Pusher](https://github.com/zerosamski/MMM-Page-Pusher).

# TODO :

* Add gif to show how to use
* Add this module to to 3rd modules MagicMirror