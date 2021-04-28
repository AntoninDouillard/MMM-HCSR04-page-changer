# MMM-HCSR04-page-changer

A module for magic mirror that uses an HCSR04 sensor to enable switching between pages.

This repo is a fork of [zerosamski/MMM-Page-Pusher](https://github.com/zerosamski/MMM-Page-Pusher).
The difference between MMM-Page-Pusher and MMM-HCSR04-page-changer is MMM-HCSR04-page-changer use
only one HCSR04 instead of two.

Current development status : WIP.

Please contact me at antonin.info@protonmail.com for any issue or question.

### How it works

Node helper gets the data from the sensor every 0.8 second via a python script. When you 'push' towards
the sensor it sends a socket notification to [MMM-Pages](https://github.com/edward-shen/MMM-pages).

You should use MMM-page-indicator and MMM-pages to enjoy this module.

### Install this module

```bash
cd ~/MagicMirror/modules/
git clone https://github.com/AntoninDouillard/MMM-HCSR04-page-changer.git
cd modules/MMM-HCSR04-page-changer
npm install
```

If this module is not working after that, install python-shell manually with npm :

```bash
npm install python-shell
```

### MagicMirror² Example Configuration

#### Example configuration for MMM-HCSR04-page-changer only

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

#### Example configuration with MMM-page-indicator and MMM-pages

```js
var config = {
    modules: [
        ...
        {
            module: "MMM-pages",
            config: {
                modules:
                    [
                        ["MMM-Formula1"], // Page 1
                        ["MMM-Strava", "MMM-Soccer"] // Page 2
                    ],
                fixed: ["clock", "MMM-page-indicator"], // Always on screen
                animationTime: 1000,
                rotationTime: 0, // 0 to use HCSR04
                homePage: 0
            }
        },
        {
	        module: 'MMM-page-indicator',
	        position: 'bottom_bar',
	        config: {
		        pages: 2
	        }
        },
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

Made with :heart: from :fr:.
