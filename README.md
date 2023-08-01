# Team Easykids-OMO 
**Team member**  : 🛠-Papangkorn Nirawatsuwan  🛠-Auttanon Jakkawarn 🛠-Noraprot Aunnahajak

  *Welcome to the documentation of Team Easykids-OMO's remarkable journey in the prestigious World Robot Olympiad 2023 (WRO). This document is a testament to the dedication, creativity, and ingenuity displayed by us, throughout this exciting and challenging competition.*

*The WRO provided a unique platform for young robotics enthusiasts like us to showcase our skills, teamwork, and problem-solving abilities. As part of this extraordinary event, we set out to design and build a robot capable of overcoming various obstacles, detecting colors, recognizing objects, and making critical decisions in real-time.*

  *Our journey began three months before the competition, and the initial stages were dedicated to meticulous planning and design. We envisioned a small yet stable robot, equipped with cutting-edge sensors and driven by powerful motor control systems, to navigate the challenging WRO tasks.*

  *Through weeks of hard work, we fine-tuned our robot's code and utilized the OpenCV library to detect and differentiate between blue and orange colors, essential for accurate path tracking. The integration of a gyroscopic sensor further enhanced our robot's agility and stability during turns and movements.*

  *Our team is immensely proud of achieving seamless cooperation between two types of motor control: DC motors for driving and servo motors for precise turning. The combination of these elements allowed our robot to maneuver swiftly and with remarkable accuracy.*

  *This documentation aims to provide an in-depth account of our robot's design, the techniques employed for color detection, algorithm development, and the challenges faced and overcome during our preparation. Additionally, we share insights into the future improvements we envision, driving us to strive for continuous innovation and excellence in the field of robotics.*

*We hope that this documentation not only serves as a testament to our hard work and determination but also inspires fellow robotics enthusiasts and future competitors. The WRO has been a transformative experience for us, fostering our passion for robotics, teamwork, and the pursuit of knowledge. We extend our gratitude to all who supported us throughout this journey, and we hope you find this documentation both informative and inspiring. Let's embark on this exhilarating journey together, exploring the realm of robotics and the incredible possibilities it offers.*
#
## 🏢 1.Working Process 👨🏼‍💼
Our journey to the World Robot Olympiad (WRO) competition was an exciting and challenging experience. As a team, we invested dedicated effort and time into the development and preparation of our robot. Here is a summary of our working process leading up to the competition:
- **Week 1-2: Designing the Robot Structure**

  We began our journey by brainstorming and designing the structure of our robot. Our main objectives were to create a compact and stable robot capable of maneuvering through various terrains and obstacles in the WRO competition. After careful consideration, we finalized the design and started gathering the required components.
  
- **Week 3-4: Code Implementation and Testing**

  With the robot structure in place, we delved into the coding phase. Our primary focus was on ensuring the robot could run smoothly and execute basic movements. We integrated the motor control and sensor interfaces and started writing the initial lines of code. As we encountered challenges, we iteratively tested and debugged the code to ensure reliability and stability.
  
- **Week 5-6: Color Detection Algorithm Development**

  As color detection was a crucial aspect of the WRO competition, we dedicated specific weeks to develop the HSV-based color detection algorithm. The first step was obtaining the initial HSV values for color detection. We allowed the user to interactively select the desired color through the robot's camera, and the algorithm printed the corresponding HSV values. We then implemented a fine-tuning process using thresholding to achieve precise color detection.
  
- **Week 7-8: Documentation and Preparing for the Competition**
  
  To document our progress and efforts, we worked on comprehensive documentation describing our robot's design, algorithm, and development process. This documentation served as a record of our journey and also provided insights into our problem-solving approach.

### ➡Practice and Learning: Continuous Improvement

Throughout the entire process, we practiced and rehearsed with our robot regularly. We aimed to solve immediate problems, refine our coding techniques, and optimize the robot's performance. Every challenge we encountered was an opportunity for learning and growth.

### ➡Final Preparations: The Road to WRO

In the weeks leading up to the competition, we intensified our practice sessions and participated in mock competitions to simulate the real event. These practice sessions allowed us to fine-tune our strategies, calibrate the robot, and gain confidence in its capabilities.

### ➡Competition Week: Putting Our Best Foot Forward

As the WRO competition week approached, we were well-prepared and determined to give our best performance. We had meticulously tested and validated our robot's color detection, navigation, and gyroscopic stabilization. Our hard work and dedication culminated in a robot that was ready to face the challenges of the competition.

Our journey to the WRO competition taught us the importance of teamwork, perseverance, and continuous improvement. Each step in our working process contributed to the success of our robot and made the entire experience memorable and rewarding. We were proud of our accomplishments and looked forward to showcasing our robot's capabilities at the prestigious WRO competition.

 #
 ## 🏠 2.Structure 🔨

 #
 ## 🤖3.How Robot Work 👷
The robot operates through a sophisticated program utilizing two types of motor control: DC motors for driving and servo motors for turning. The program employs the power of OpenCV to check for blue and orange colors, enabling the robot to detect the distance of the line and make precise turns. Additionally, a distance sensor aids in detecting the edge of the field, allowing the robot to navigate within the confines of the designated area.
With the newly incorporated gyroscope, the robot gains increased stability and agility during turns. The gyroscope facilitates fast and stable rotations, enhancing the overall performance of the robot.
To ensure seamless navigation, the robot also utilizes OpenCV Color detection to identify traffic signs. Upon detecting a traffic sign, the program commands the robot to reverse itself, enabling it to adjust its direction and follow the appropriate path.
Through the fusion of advanced motor control, real-time image processing with OpenCV, and the added stability from the gyroscope, our robot confidently maneuvers through the competition arena. This well-crafted program allows the robot to accurately detect colors, follow lines, and respond swiftly to traffic signs and obstacles, making it a formidable contender in the World Robot Olympiad competition.
#
## 🚦4. Selection Color Sensor🌈
Choosing the right sensor for color detection in a robotics competition like the World Robot Olympiad (WRO) is a critical decision that can significantly impact the robot's performance and success. In this case, my team has two options: an RGB sensor and a camera with OpenCV. Both options have their strengths and weaknesses, and it's essential to weigh them carefully before making a final decision.
### ▶️RGB Sensor : 
An RGB sensor is specifically designed to detect and differentiate colors. It consists of three individual sensors that measure the intensity of red, green, and blue light in the environment. By combining the readings from these sensors, the RGB sensor can determine the color of an object. Here are some key advantages of using an RGB sensor:

- **(1)__Color Detection:**	
 As mentioned earlier, the primary purpose of an RGB sensor is color detection. It can accurately identify a wide range of colors, making it suitable for tasks that require precise color recognition, such as sorting colored objects or following colored paths.
- **(2)__Easy Integration with Microcontrollers:**
 Most RGB sensors are designed to work seamlessly with popular microcontrollers like Arduino or Raspberry Pi. This integration simplifies the process of connecting the sensor to the robot's control system and accessing color data.
- **(3)__Compact and Lightweight:**
 RGB sensors are often compact and lightweight, which is essential for mobile robots like those used in WRO competitions. The sensor's size and weight won't impede the robot's movement or agility.

![GY-31](https://github.com/Beam1pnzaza/WRO.Easykids-OMO/assets/86812911/cd981931-911f-4a86-a269-eb895a152888)

### ▶️Camera with OpenCV:
Using a camera with OpenCV for color detection provides additional capabilities and flexibility compared to an RGB sensor. OpenCV is an open-source computer vision and image processing library that allows robots to process visual information from a camera. Here are the advantages of using a camera with OpenCV:

- **(1)__Real-Time Processing:**	
 One of the main advantages of using OpenCV with a camera is its ability to perform real-time image processing. This means the robot can process color information from the camera feed on the fly, enabling quicker reactions and decisions.
- **(2)__Color Range:**
 OpenCV provides more advanced color range detection compared to a simple RGB sensor. You can implement custom algorithms to detect specific colors or color ranges, fine-tuning the robot's color recognition capabilities.
- **(3)__Object Detection:**
  With a camera and OpenCV, you can go beyond simple color detection and implement more complex object detection algorithms. This allows the robot to recognize and interact with specific objects or shapes in the environment, such as detecting and avoiding obstacles like cones.
- **(4)__Versatility:**
  Using a camera with OpenCV opens up a world of possibilities beyond color detection. The robot can perform various computer vision tasks, such as pattern recognition, image filtering, and edge detection, which may be beneficial for certain WRO challenges.

![images](https://github.com/Beam1pnzaza/WRO.Easykids-OMO/assets/86812911/afb9d175-7f5a-434c-bb8e-b494b190aa99)

### ➡We finally made a choice to choose camera with open cv:
Considering the advantages of both options, the camera with OpenCV emerges as the more advantageous choice for several reasons:

- **(1)__Real-Time Processing:**	
In fast-paced competitions like WRO, real-time processing is crucial. The camera with OpenCV provides faster and more sophisticated color processing, enabling the robot to make more informed decisions in real-time.
- **(2)__Color Range and Object Detection:**
 OpenCV's flexibility allows your team to implement custom color range detection and more complex object detection algorithms. This adaptability enhances the robot's color recognition capabilities and its ability to interact with the environment effectively.
- **(3)__Versatility for Future Challenges:**
 Using OpenCV and a camera provides versatility for future challenges beyond WRO. My team can explore various computer vision tasks and expand the robot's capabilities in other robotics projects.

![Screenshot 2023-08-01 140550](https://github.com/Beam1pnzaza/WRO.Easykids-OMO/assets/86812911/36ed7229-6d0f-4f47-8332-ed26ae4c6656)

**In conclusion, while an RGB sensor has its advantages, the camera with OpenCV offers superior performance, real-time processing, and more advanced color range and object detection capabilities. These factors make it the better choice for color detection in your WRO robot, giving my team a competitive edge in the competition and setting the stage for future robotics endeavors.**

#
## 5. Technique Detect 🔍
In the field of robotics, color detection plays a crucial role in various applications, such as object recognition, obstacle avoidance, and path planning. One popular method for color detection is using the Hue, Saturation, and Value (HSV) color space. This technique offers several advantages over other color spaces, making it a popular choice for many robotic applications. Additionally, using thresholding with HSV values allows for more accurate color detection, enabling robots to make precise decisions based on the detected colors.
### ➡HSV Color Space: 
HSV is a color space that represents colors in terms of their human perception, making it more intuitive and easier to work with than the RGB color space. It consists of three components:
- **【﻿Ｈ】_(Hue):**	Represents the color's dominant wavelength and is often visualized as a color wheel, ranging from 0 to 360 degrees. It allows for easy identification of different colors without considering their brightness or intensity.
- **【﻿Ｓ】_(Saturation):** Indicates the purity of the color, with 0 representing grayscale and 1 representing the most vibrant color. Saturation controls the amount of white light mixed with the color, affecting its intensity.
- **【﻿Ｖ】_(Value):** Represents the brightness of the color, with 0 being black and 1 being the brightest possible color. It determines how light or dark the color appears.

  ![HSV Graph](https://github.com/Beam1pnzaza/WRO.Easykids-OMO/assets/86812911/f8efcf23-75eb-43d5-963e-8cf863487526)

  **HSV is particularly advantageous in robotics because it separates the color information from brightness, making it more robust in varying lighting conditions.**
  
### ▶️ Step 1: Obtaining Initial HSV Values
In the first step of our color detection technique, we utilize the robot's camera along with OpenCV or a similar image processing library to obtain the initial HSV (Hue, Saturation, Value) values for the desired color. The process begins with the operator aiming the camera at the object or color they want the robot to detect. With a simple click on that specific color in the camera's view, the first code extracts the corresponding HSV values of the clicked pixel. These values are then displayed on the screen, providing crucial information about the color we want the robot to identify.

By obtaining the initial HSV values directly from the real-world environment, we ensure that the robot's color detection is tailored to the specific conditions and lighting present at the time of calibration. This step allows for customization of the color range and sets the foundation for accurate color detection in subsequent stages.

![Screenshot 2023-08-01 145657](https://github.com/Beam1pnzaza/WRO.Easykids-OMO/assets/86812911/31fc710f-22d4-4542-8c39-61e1cfcebd93)

### ▶️ Step 2: Fine-Tuning HSV Values with Thresholding
The second step in our color detection technique involves fine-tuning the initially obtained HSV values to optimize the detection accuracy. To achieve this, we implement a user interface that displays the live camera feed along with adjustable slide bars representing the HSV thresholds. The operator can now iteratively adjust these slide bars to modify the HSV range and fine-tune the color detection process.

With the camera feed being displayed, the operator observes the results of the color detection and makes incremental adjustments to the HSV values using the slide bars. The objective is to refine the color detection threshold to precisely isolate the desired color while minimizing false detections of similar hues or background noise.

Through this iterative process, the operator can visually assess the detection performance and dynamically adapt the HSV values to cater to different lighting conditions or variations in the color's appearance. This level of customization ensures robust and reliable color detection even in challenging environments.

Once the operator achieves an optimal HSV range that accurately detects the desired color, the fine-tuned HSV values are saved. These refined HSV thresholds will be used in the robot's while loop to continuously process the camera feed, enabling real-time color detection during the robot's operation

![Screenshot 2023-08-01 150627](https://github.com/Beam1pnzaza/WRO.Easykids-OMO/assets/86812911/9117b454-a5c2-4952-9235-0ef24d3c305f)

**In conclusion, the two-step technique of obtaining initial HSV values and fine-tuning them through thresholding empowers our robot with accurate and adaptable color recognition capabilities. By customizing the color detection process to the specific environment and adjusting it in real-time, our robot can reliably identify the desired color, making informed decisions and executing tasks effectively in diverse scenarios. The combination of initial HSV values and fine-tuning ensures that our robot remains versatile and responsive to changes, allowing it to excel in a wide range of applications where accurate color detection is essential.**

#
## 6.Algorithm Development 
Our algorithm focuses on achieving stable and efficient control for our robot in the World Robot Olympiad (WRO) competition. The key components of our algorithm are color detection using HSV (Hue, Saturation, Value) values and gyroscopic stabilization. By combining these elements, our robot can navigate with precision and stability. 
- **(1)__Color Detection using HSV:** We start by obtaining the initial HSV values for color detection. Through the robot's camera, we enable the user to select the desired color by clicking on it. The algorithm then prints the corresponding HSV values, which serve as the basis for further processing.
- **(2)__Fine-Tuning HSV Values with Thresholding:** To improve color detection accuracy, we implement a second code with a slider interface. We take the initial HSV values obtained from the first step and adjust them using the sliders. The goal is to find the optimal HSV range that isolates the desired color accurately under different lighting conditions.
- **(3)__Gyroscopic Stabilization:** We integrate a gyroscope with our robot to achieve stability during turns and movements. The gyroscope provides real-time data on the robot's angular velocity, enabling us to maintain balance during high-speed maneuvers.
- **(4)__Turn and Drive Algorithm:** Based on the fine-tuned HSV values, we implement a while loop to control the robot's movements. When the robot detects the desired color within the HSV range, the algorithm dictates the appropriate action – whether to turn left, turn right, drive forward, or stop.
- **(5)__Feedback Loops:** To ensure precision in movements, we employ feedback loops that continuously update the robot's position and correct any deviations from the desired path. These feedback loops help the robot maintain accuracy during complex maneuvers.
- **(6)__Integration of Gyroscope and Camera Data:** By fusing data from the gyroscope and camera, our algorithm enables the robot to make informed decisions. It adjusts movements in real-time based on detected colors and gyroscopic feedback.
- **(7)__Path Planning and Optimization:** For tasks that require precise navigation, we implement path planning algorithms. By combining sensor data, feedback from the gyroscope, and knowledge of the competition field, our robot optimizes its path to reach specific locations efficiently.
- **(8)__Efficient Execution:** Our algorithm is designed for efficient execution, utilizing optimized data structures and algorithms to minimize computation time and memory usage. This enables the robot to respond quickly and perform tasks with minimal delay.
- **(9)__Real-Time Processing:** The algorithm is engineered for real-time processing to provide immediate responses to changing conditions. This ensures the robot's agility and responsiveness during the competition.
  
![1  Color Detection using HSV](https://github.com/Beam1pnzaza/WRO.Easykids-OMO/assets/86812911/4bac3af5-2a08-418d-ae6f-bb16a446b702)

**In conclusion, our Algorithm Development of Code combines color detection using HSV values and gyroscopic stabilization to achieve stable and efficient robotics control. This approach allows our robot to navigate accurately and make informed decisions, enhancing its performance in the WRO competition.**
