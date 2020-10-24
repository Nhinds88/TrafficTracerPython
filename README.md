# Python Files for Traffic Tracer Python Application

![trafficTracer_GIF_800x533_No_BG](https://user-images.githubusercontent.com/48838759/97059888-a5e3dd00-1546-11eb-9cd8-d918441185c0.gif)

Traffic Tracer is a Python and Web Application that seeks to use a merchants pre-existing camera system to gather foot traffic data and present this data in friendly easy to read manner.

This a the Python application that handles the video processing. 
There are several versions of the applicaion. 
  
  1. The Admin version used for clients with modern camera systems that can provide a stream, this is also used for testing the parameters needed for a customers camera       as it is more flexible.
  
  2. The Client version usd for clients with older camera systems that cannot provide a stream to Traffic Tracer. this version has the hard coded parameters for the customers camera and only requires the customer to enter the date and start time of the video. 
  
  3. the raw python scripts used for feature development.


To run you'll need a few libraries:

pip install scipy
pip install numpy
pip install opencv-contrib-python
pip install mysql-connector-python
