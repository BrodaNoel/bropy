# BroPySky
Suite for PyInTheSky projects.
The community call `#PyInTheSky` all projects when in some way, you put your RaspberryPy in the sky for taking photos, or atmospheric measures.

## Installation
* `cd ~/bropy`
* `bropy install bropysky`

## Run project
Create the configuration file.
The configuration file should be called `config.json` and should be inside `/projects/bropysky`.

There is a `config.example.json` file to use as example.
```JSON
{
	"modules": {
		"gps": "gy-gps6mv1"
	}
}
```