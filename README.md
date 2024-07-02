Sure! Here is an updated README file for the GitHub repository, incorporating the new information and removing the existing methods section as requested.

---

# Animal Intrusion Detection and Deterrence System

## Overview

The Animal Intrusion Detection and Deterrence System is designed to address the problem of animal intrusions in agricultural and residential areas. This system leverages advanced technologies such as ultrasonic radar sensors, thermal cameras, and deep learning to detect and humanely deter animals, protecting crops and property while ensuring safety.

## Motivation

Farmers face significant economic losses and physical danger due to animal intrusions. Traditional methods like fencing and manual monitoring are often ineffective and costly. This project aims to provide an automated, efficient, and humane solution to mitigate these challenges.

## Objectives

1. **Reduce Crop and Property Damage**: Implement an effective system to minimize economic losses caused by animal intrusions.
2. **Enhance Safety and Security**: Provide a safer environment for farmers, their families, and residential property owners.
3. **Utilize Advanced Technologies**: Integrate ultrasonic radar sensors, thermal cameras, and deep learning algorithms for real-time detection and identification.

## Proposed System

### Machine Learning Model Development
- **Custom Dataset Creation**: Curated dataset of animal images and videos, annotated for training.
- **YOLOv8 Algorithm**: Trained for real-time detection and classification of humans, dogs, rabbits, hens, cats, and pigeons.

### Hardware Integration
- **Ultrasonic Sensors (HC-SR04)**: Detect nearby objects using ultrasonic waves.
- **FLIR AX5 Series Thermal Cameras**: Detect infrared radiation for identifying animals based on body heat.
- **Micro Servo Motor**: Controls rotation of sensors and cameras for comprehensive coverage.

### System Operation
- **Control Hub**: Arduino Uno orchestrates the operation of all components.
- **Continuous Scanning**: Ultrasonic radar and thermal cameras continuously monitor the area.
- **Detection and Analysis**: Identified objects trigger detailed analysis and classification.
- **Deterrence**: Ultrasonic frequencies tailored to detected animals are emitted to deter them.
- **Data Logging and Alerts**: Logs intrusion events and sends alert notifications to users.
- **Monthly Reporting**: Generates reports summarizing intrusion events and patterns.

## System Architecture

The system architecture integrates various hardware components, controlled by an Arduino Uno, ensuring reliable and efficient operation.

## Frequencies for Deterrence

| Animal    | Frequency (kHz) |
|-----------|------------------|
| Human     | 25               |
| Dog       | 40               |
| Rabbit    | 30               |
| Hen       | 35               |
| Cat       | 40               |
| Pigeon    | 35               |

## Installation

### Prerequisites

- Python 3.10 or higher
- Arduino IDE

### Python Libraries

1. **PySerial**: Library for serial communication with Arduino.

    ```bash
    pip install pyserial
    ```

2. **Python Mailing Library**: Library for sending email notifications.

    ```bash
    pip install secure-smtplib
    ```

3. **YOLOv8**: Follow the official YOLOv8 installation instructions for setting up the machine learning model.

### Arduino Libraries

1. **Ultrasonic Sensor Library**: Required for handling ultrasonic sensor data.

    ```bash
    # Open Arduino IDE, go to Sketch > Include Library > Manage Libraries
    # Search for "NewPing" and install it
    ```

2. **Servo Motor Library**: Required for controlling the servo motors.

    ```bash
    # Open Arduino IDE, go to Sketch > Include Library > Manage Libraries
    # Search for "Servo" and install it
    ```

### Connecting Hardware

1. **Connect Ultrasonic Sensors**: Attach the HC-SR04 sensors to the Arduino Uno as per the provided circuit diagram.
2. **Connect Thermal Camera**: Attach the FLIR AX5 series thermal cameras to the Arduino Uno.
3. **Connect Servo Motor**: Attach the micro servo motors to the Arduino Uno.

### Running the System

1. **Upload Arduino Code**: Open the Arduino IDE, load the provided Arduino sketch, and upload it to the Arduino Uno.
2. **Run Python Script**: Execute the Python script to start monitoring and detection.

    ```bash
    python arduinoPYserial.py
    ```
3.Make sure Serial monito is off as it may not work with pyserial simultaneously.

## Bottlenecks

1. **Permissions**: Required from the animal husbandry department for testing.
2. **Cost and Availability**: Ultrasonic transducers are rare and expensive.
3. **Lack of Diverse Datasets**: Collaboration needed to gather comprehensive animal data.

## Future Scope

1. **IoT Integration**: Remote monitoring and control via smartphones or computers.
2. **Solar-Powered Operation**: Sustainable power source for remote areas.
3. **Advanced Data Analytics**: Enhanced visualization tools for better understanding of intrusion patterns.
4. **Integration with Drones**: Expanded surveillance area and access to hard-to-reach places.
5. **Multi-Species Deterrence**: Tailored deterrence methods for a wider variety of animal species.

## Product Images


![image](https://github.com/Brucely17/Agri-Animal-IntrusionDetection-Deternece/assets/111076441/6ed99113-078b-47e8-a2c6-566718725a00)
*Figure 1: Architecture*



![image](https://github.com/Brucely17/Agri-Animal-IntrusionDetection-Deternece/assets/111076441/4b35845b-a8a9-4439-b8ba-f6e09c03d7d5)

*Figure 2: Flow Chart*


![image](https://github.com/Brucely17/Agri-Animal-IntrusionDetection-Deternece/assets/111076441/866a97ca-9a86-462b-800d-e18d53bc5641)

*Figure 3: Arduino Uno*

![image](https://github.com/Brucely17/Agri-Animal-IntrusionDetection-Deternece/assets/111076441/e2bf609d-6adc-4694-8d7c-220955a35f79)

*Figure 4: Frequency Oscillator*

## Conclusion

The Animal Intrusion Detection and Deterrence System offers a significant advancement in protecting agricultural fields from wildlife intrusions. It combines ultrasonic sensors, thermal cameras, and machine learning techniques to ensure high precision in detecting and classifying animals. The system is cost-effective, scalable, and promotes sustainable farming practices by enabling peaceful coexistence with wildlife.

## Contact

For more information, please contact:

- **Nandhana S** - nandhana@example.com
- **Purushothaman P** - purushothaman2110796@ssn.edu.in
- **Vijay V** - vijay@example.com
- **Ranjith S** - ranjith2112052@ssn.edu.in

---

Feel free to modify the contact information, installation steps, and any other details as needed for your specific project and team. Don't forget to add the actual image files in the `images` directory in your repository.
