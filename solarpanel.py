# *-* coding: utf-8 *-*
# Author: @2sayle
# Date: 2024-29-06
# Version: 1.0
# Description: A simple model for solar panels

import math

class SolarPanel:
    def __init__(self, area, efficiency, tilt, orientation):
        self.area = area                # m^2
        self.efficiency = efficiency    # %
        self.tilt = tilt                # degrees 
        self.orientation = orientation  # degrees (0 = South, 90 = West, 180 = North, 270 = East)

    def computeIrradiance(self, hour, day_of_year, latitude):
        # Simplified irradiance model
        # Based on the solar declination angle and the hour angle
        declination = 23.45 * math.sin(2 * math.pi / 365 * (284 + day_of_year))
        hour_angle = 15 * (hour - 12)

        sin_altitude = math.sin(math.radians(latitude)) * math.sin(math.radians(declination)) + \
                       math.cos(math.radians(latitude)) * math.cos(math.radians(declination)) * \
                       math.cos(math.radians(hour_angle))
        
        altitude = math.degrees(math.asin(sin_altitude))

        if altitude > 0:
            return 1000 * sin_altitude # W/m^2
        else:
            return 0
        
    def computePower(self, irradiance):
        incidence_angle = self.tilt - 90 + math.degrees(math.asin(irradiance / 1000))
        angle_factor = max(0, math.cos(math.radians(incidence_angle)))

        production = self.area * irradiance * self.efficiency / 100 * angle_factor
        return production
    