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
### RGB Sensor : 
An RGB sensor is specifically designed to detect and differentiate colors. It consists of three individual sensors that measure the intensity of red, green, and blue light in the environment. By combining the readings from these sensors, the RGB sensor can determine the color of an object. Here are some key advantages of using an RGB sensor:

- **(1)__Color Detection:**	
 As mentioned earlier, the primary purpose of an RGB sensor is color detection. It can accurately identify a wide range of colors, making it suitable for tasks that require precise color recognition, such as sorting colored objects or following colored paths.
- **(2)__Easy Integration with Microcontrollers:**
 Most RGB sensors are designed to work seamlessly with popular microcontrollers like Arduino or Raspberry Pi. This integration simplifies the process of connecting the sensor to the robot's control system and accessing color data.
- **(3)__Compact and Lightweight:**
 RGB sensors are often compact and lightweight, which is essential for mobile robots like those used in WRO competitions. The sensor's size and weight won't impede the robot's movement or agility.

### Camera with OpenCV:
Using a camera with OpenCV for color detection provides additional capabilities and flexibility compared to an RGB sensor. OpenCV is an open-source computer vision and image processing library that allows robots to process visual information from a camera. Here are the advantages of using a camera with OpenCV:

- **(1)__Real-Time Processing:**	
 One of the main advantages of using OpenCV with a camera is its ability to perform real-time image processing. This means the robot can process color information from the camera feed on the fly, enabling quicker reactions and decisions.
- **(2)__Color Range:**
 OpenCV provides more advanced color range detection compared to a simple RGB sensor. You can implement custom algorithms to detect specific colors or color ranges, fine-tuning the robot's color recognition capabilities.
- **(3)__Object Detection:**
  With a camera and OpenCV, you can go beyond simple color detection and implement more complex object detection algorithms. This allows the robot to recognize and interact with specific objects or shapes in the environment, such as detecting and avoiding obstacles like cones.
- **(4)__Versatility:**
  Using a camera with OpenCV opens up a world of possibilities beyond color detection. The robot can perform various computer vision tasks, such as pattern recognition, image filtering, and edge detection, which may be beneficial for certain WRO challenges.

### ➡We finally made a choice to choose camera with open cv:
Considering the advantages of both options, the camera with OpenCV emerges as the more advantageous choice for several reasons:

- **(1)__Real-Time Processing:**	
In fast-paced competitions like WRO, real-time processing is crucial. The camera with OpenCV provides faster and more sophisticated color processing, enabling the robot to make more informed decisions in real-time.
- **(2)__Color Range and Object Detection:**
 OpenCV's flexibility allows your team to implement custom color range detection and more complex object detection algorithms. This adaptability enhances the robot's color recognition capabilities and its ability to interact with the environment effectively.
- **(3)__Versatility for Future Challenges:**
 Using OpenCV and a camera provides versatility for future challenges beyond WRO. My team can explore various computer vision tasks and expand the robot's capabilities in other robotics projects.

**In conclusion, while an RGB sensor has its advantages, the camera with OpenCV offers superior performance, real-time processing, and more advanced color range and object detection capabilities. These factors make it the better choice for color detection in your WRO robot, giving my team a competitive edge in the competition and setting the stage for future robotics endeavors.**
![Screenshot_2023-08-01_110051-removebg-preview](https://github.com/Beam1pnzaza/WRO.Easykids-OMO/assets/86812911/061ce6a1-8cbe-48dc-808f-c45b99cb54ef)

