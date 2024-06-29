# Solar Panel Simulator

This project is a Solar Panel Simulator that calculates and visualizes the irradiance and power production of a solar panel throughout the year. It takes into account factors such as panel characteristics, geographical location, and time of day to provide accurate simulations.

## Features
- Simulates solar panel performance for a full year
- Calculates irradiance based on day of the year, time, and latitude
- Computes power production considering panel efficiency and tilt
- Generates plots for annual irradiance and power production
- Provides basic statistical analysis of the results

## Requirements
- Python 3+
- matplotlib
- numpy

## Installation
1. Clone this repository:
```bash
https://github.com/2sayle/Solar_Panel_Simulator.git
```
2. Navigate to the project directory:
```bash
cd Solar_Panel_Simulator
```
3. Install the required packages:
```bash
pip install matplotlib numpy
```

## Usage
Run the main script:
``` 
python main.py
```
This will generate plots showing the annual irradiance and power production for the specified solar panel and location.

## Configuration
You can modify the following parameters in `main.py`:
- Solar panel characteristics (area, efficiency, tilt, orientation)
- Time of day for the simulation
- Latitude of the location

## File Structure
- `main.py`: The main script to run the simulation and generate plots
- `solarpanel.py`: Contains the `SolarPanel` class with core calculation methods
- `README.md`: This file, containing project documentation

## Contributing
Contributions to improve the simulator are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
- @2sayle

## Acknowledgments
- Thanks to the matplotlib and numpy teams for their excellent libraries
- Inspired by real-world solar energy systems and the need for accessible simulation tools

## Version History
- 1.1: Added annual plotting and basic statistics (2024-06-29)
- 1.0: Initial release with basic simulation capabilities (2024-06-29)

## Future Improvements
- Add more environmental factors (e.g., temperature, cloud cover)
- Implement different types of solar panels
- Create a user-friendly GUI for easier parameter adjustment
- Extend the simulation to include battery storage systems

## Sources
- Declination model based on : http://www.heliodon.net/downloads/Beckers_2010_Helio_007_fr.pdf
