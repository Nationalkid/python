================
Pyqt and plotly
================

The script gets an input data (excel file) and generated an
interactive Likert scale plot using the plotly library

An example using the likert scale
----------------------------------

The example is based on a small sample of data of Viallauex's thesis.
The input data was produced after qualitative survey to understand people's perception on
how much they value ecosystem services towards some landscapes.

The ecosystem services were the following :

- Food
- Wood
- Water_supply
- Regulation
- Air_quality
- Scenic_beauty

With four possible land scapes :

- Agriculture
- Forest
- Settlement
- Grassland

This script creates a Qt GUI (trough PyQT) where the user is able to select his data, the ecosystem service.
The GUI allows grouping people per gender, age, age_class, education and activity.