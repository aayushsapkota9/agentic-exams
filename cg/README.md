# Computer Graphics (CMP 234)

**Pokhara University**  
**Faculty of Science and Technology**

| Attribute | Details |
| :--- | :--- |
| **Course Code** | CMP 234 |
| **Course Title** | Computer Graphics |
| **Nature of Course** | Theory and Practical (3-1-2) |
| **Level** | Bachelor (Program: BE) |
| **Total Lectures** | 45 Hours |
| **Full Marks** | 100 (Theory: 50, Practical: 50) |
| **Pass Marks** | 45 |

---

## 1. Course Description
This course intends to provide students with an in-depth knowledge of a machine’s perception of visual information for storing, accessing and manipulating visual representations of graphical objects and scenes. The course contents cover theoretical, practical, mathematical and algorithmic aspects of concepts such as graphical hardware, two-dimensional and three-dimensional representations of graphical objects, the use of techniques such as projection, visible surface detection and lightning effects. The main aim of the course is also to impart knowledge to students regarding the techniques used for incorporating visual realism in the computer-generated images and scenes portrayed on a display device.

## 2. General Objectives
The course is designed with the following objectives:
* To make the students familiar with the technologies used for representing and rendering of graphical objects and scenes in a computer system.
* To equip students with necessary skills and knowledge of Two-dimensional and Three-dimensional graphics necessary for viewing and performing transformations.
* To provide students with a good amount of knowledge of algorithms and approaches used to incorporate maximum amount of visual realism in the computer-generated graphical scenes and objects.
* To familiarize students with the graphical standards used for building platform-independent portable software.

## 3. Methods of Instruction
As the course consists of theoretical, mathematical and practical aspects of Computer Graphics, the delivery needs to include lecture, tutorial, and practical classes. Apart from that, in order to share knowledge and assimilate new ideas and emerging trends, students can be involved in group discussions and presentations pertaining to the field of Computer Graphics. Short quizzes can be held in the class to check the students’ level of comprehension. Project work can be assigned to students to come up with a graphical software product that demonstrates their level of understanding of the contents studied in the course.

---

## 4. Contents in Detail

| Unit | Specific Objectives | Contents | Resources |
| :--- | :--- | :--- | :--- |
| **Unit 1: Overview of Computer Graphics and Graphics Systems** (7 hrs) | Provides a brief introduction of the field of Computer Graphics and familiarize students with basic graphics hardware and software. Enhances understanding of technology used for producing graphical output. | 1.1 Introduction, Applications and Recent trends <br> 1.2 Interactive Input Devices <br> 1.3 Display Devices, Color Monitors, Hard Copy Devices <br> 1.4 Raster and Random Scan Systems and Architectures <br> 1.5 Video Controller <br> 1.6 Use of Digital to Analog Converter and Frame Buffer Organization <br> 1.7 Graphics Software, Modern Graphics Hardware (GPU) | [Syllabus](chap1/chap1-syllabus.md) \| [Questions](chap1/chap1-qns.md) |
| **Unit 2: Scan Conversion Algorithms** (7 hrs) | Learn about various scan conversion and area filling algorithms. Implement these algorithms using a programming language. Generate output primitives and fill them with specified intensities. | 2.1 Scan Conversion <br> 2.2 Line Drawing Algorithms (DDA, Bresenham's) <br> 2.3 Circle Generation Algorithm <br> 2.4 Ellipse Generation Algorithm <br> 2.5 Filled Area Primitives (Scan Line Polygon Fill, Boundary Fill, Flood Fill) | [Syllabus](chap2/chap2-syllabus.md) \| [Questions](chap2/chap2-qns.md) |
| **Unit 3: Two Dimensional Geometric Transformations and Viewing** (8 hrs) | Reposition and resize objects in 2D scene. Viewing routines that convert a world coordinate scene description to a display for an output device. | 3.1 2D Transformations (Translation, Rotation, Scaling, Shearing, Reflection) <br> 3.2 Matrix Representations <br> 3.3 Homogeneous Coordinate System <br> 3.4 Composite Transformations <br> 3.5 Windowing Concepts, 2D Viewing Pipeline <br> 3.6 Window to Viewport Transformation <br> 3.7 Line Clipping: Cohen-Sutherland <br> 3.8 Polygon Clipping: Sutherland-Hodgeman | [Syllabus](chap3/chap3-syllabus.md) \| [Questions](chap3/chap3-qns.md) |
| **Unit 4: Graphics in Three Dimensions** (8 hrs) | Extensions of 2D methods for 3D geometric transformation. Apply knowledge of 3D rendering and transformations for representing objects more accurately. | 4.1 3D Coordinate Systems <br> 4.2 3D Transformations (Translation, Rotation, Scaling, Reflection) <br> 4.3 3D Representations (Polygon Surfaces, Cubic Spline, Bezier Curve/Surface, Fractal Geometry) <br> 4.4 3D Viewing Transformation and Pipeline <br> 4.5 Projections (Parallel, Perspective) <br> 4.6 Clipping in 3D | [Syllabus](chap4/chap4-syllabus.md) \| [Questions](chap4/chap4-qns.md) |
| **Unit 5: Visual Realism** (7 hrs) | Techniques for visual realism. Visible surface detection techniques for realistic displays. Light intensities using lighting/shading models. | 5.1 Hidden Surface Removal (Back-Face Detection, Depth Buffer, A-buffer, Scan Line, Depth Sorting) <br> 5.2 Illumination and Shading (Ambient, Diffuse, Specular/Phong, Constant, Gouraud, Phong, Fast Phong) <br> 5.3 Color Models (RGB, CMYK) | [Syllabus](chap5/chap5-syllabus.md) \| [Questions](chap5/chap5-qns.md) |
| **Unit 6: Graphical Standards** (4 hrs) | Use of graphical standards for software portability. Basic structure/format of graphical files and data visualization. Writing portable graphical programs. | 6.1 Need for Machine Independent Graphical Languages <br> 6.2 Graphical Standards: PHIGS, GKS <br> 6.3 Graphics Software Standards and Language Binding <br> 6.4 Overview of Graphics File Formats <br> 6.5 Visualization of Data Sets | [Syllabus](chap6/chap6-syllabus.md) \| [Questions](chap6/chap6-qns.md) |
| **Unit 7: Introduction to OpenGL** (4 hrs) | Learn library functions for rendering and geometric transformations. Write programs to draw primitives and perform basic transformations. | 7.1 Overview and Basic Architecture of OpenGL <br> 7.2 GL Related Libraries <br> 7.2.1 Drawing Basic Output Primitives and Polygons <br> 7.2.2 Call Back Functions and Input Handling <br> 7.2.3 Basic Transformations <br> 7.2.4 Projections and Lighting | [Syllabus](chap7/chap7-syllabus.md) \| [Questions](chap7/chap7-qns.md) |

---

## 5. List of Tutorials (15 Hours)
The following tutorial activities should be conducted to cover all required contents:

1. Solving problems related to Raster Graphics system (frame buffer size, color manipulation, aspect ratio, refresh rate, resolution, etc.).
2. Identifying points for digitizing line, circle, and ellipse using studied algorithms.
3. Solving problems related to 2D Transformations and Matrix Compositions (fixed point scaling, pivot point rotation, reflection about arbitrary lines, etc.).
4. Mapping object descriptions from window to viewport and clipping line segments.
5. Solving problems related to 3D Transformations.
6. Computing points for constructing a Bezier Curve with given control points.
7. Solving problems related to Parallel and Perspective Projection.
8. Determining surface normal of polygons and visibility using Back-face detection.
9. Determining averaged intensity at a point of a polygon using Gouraud Shading.

## 6. Practical Work
Students are required to implement 2D and 3D graphics algorithms using **C/C++ and OpenGL**.

### Lab Assignments:
1. Familiarization with tools for implementing algorithms.
2. Drawing a straight line using DDA and Bresenham’s algorithms.
3. Digitizing a circle using Circle Drawing Algorithm.
4. Digitizing an ellipse using Ellipse Drawing Algorithm.
5. Performing 2D transformations on drawn objects.
6. Filling objects using Boundary Fill and Flood Fill approaches.
7. Drawing projected views of 3D objects (Perspective and Parallel) with 3D transformations.
8. Drawing smooth curves using Bezier curves with designated control points.
9. Using OpenGL library functions for primitives, transformations, and algorithm implementation.

### Project Work:
*   **Team Size:** 4-5 members.
*   **Goal:** Demonstrate knowledge through Games or Graphical Simulations.
*   **Platforms:** Explore new languages or platforms (Unity, Unreal Engine, OpenGl, etc.).

---

## 7. Evaluation System

### Internal Evaluation (50 Marks)
| Category | Component | Weight |
| :--- | :--- | :--- |
| **Theory (30)** | Attendance & Participation | 10% |
| | Assignments | 20% |
| | Presentations/Quizzes | 10% |
| | Internal Assessment | 60% |
| **Practical (20)** | Attendance & Participation | 20% |
| | Lab/Project Report | 30% |
| | Practical Exam/Project | 30% |
| | Viva | 20% |

### External Evaluation (50 Marks)
*   **Semester-End Examination:** 50 Marks

> [!IMPORTANT]
> **Student Requirements:** Each student must secure at least 45% marks in internal evaluation with 80% attendance to be eligible for the semester-end examination (NQ rule applies).

---

## 8. Prescribed Books
### Prescribed Text Book
*   **Donald Hearn and M. Pauline Baker:** *Computer Graphics C Version*, Prentice-Hall.

### Reference Books
*   **Donald Hearn and M. Pauline Baker:** *Computer Graphics with OpenGL*, Prentice-Hall.
*   **James D. Foley et al.:** *Computer Graphics: Principles and Practice in C*, Addison-Wesley.
*   **Mason Woo et al.:** *OpenGL Programming Guide: The Official Guide to Learning OpenGL*, LPE Pearson Edition Asia.
