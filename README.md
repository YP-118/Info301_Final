# **Uncovering Geographic Variability in Breast Cancer Biomarkers: Integrating Machine Learning and Interactive Visualizations for Global Insights**

## Project Information

- **Authors**: Yian Pei,  Munkh-Orshikh Munkhbold, Lauris Vo

- **Instructor**: Professor Luyao Zhang, Duke Kunshan University

- **Disclaimer**: Submissions to the Final Project for INFOSCI 301: Data Visualization and Information Aesthetics at Duke Kunshan University final project instructed by Prof. Luyao Zhang at Duke Kunshan University in Autumn 2024.

- **Acknowledgments**: 

This project represents the culmination of collaborative effort, thoughtful guidance, and the invaluable support of various individuals and resources. We wish to express our sincere gratitude to the following:
   - **Professor and Course Support**
      - **Professor Luyao (Sunshine) Zhang**: Your insightful guidance, engaging lectures, and unwavering support throughout the INFOSCI 301: Data Visualization and Information Aesthetics course were instrumental in shaping this project. Your encouragement to push the boundaries of our learning was deeply inspiring.
      - **Classmates**: A special thanks to our peers in INFOSCI 301 for fostering a collaborative and supportive learning environment. Your feedback, discussions, and shared enthusiasm greatly enriched the quality of our project.
   - **Open-Source Tools and Libraries** This project heavily relied on the contributions of the open-source community. The following tools and frameworks were critical to our success:
      - **Python Libraries**:
         - `pandas`, `numpy`, and `matplotlib` for data manipulation and basic visualizations.
         - `seaborn` and `plotly` for enhanced plotting capabilities and interactive visuals.
         - `networkx` and `dash` for creating network diagrams and web-based visualizations.
      - **Gephi**: For advanced network analysis and modularity-based clustering.
      - **GitHub**: For version control, collaboration, and hosting the repository. 
   - **AAA Dataset**: A pivotal dataset for misinformation analysis, available through the Sustainable Finance Lab at the University of Zurich.
   - **AAA Dataset**: Behavioral and demographic data, which provided valuable insights into misinformation susceptibility.
   - **AIGC Tools**: Tools such as ChatGPT contributed to structuring, refining, and enhancing our documentation and research outputs.

- **Project Summary**:
<p align="center">
  <kbd>
    <img src="figure1.png" alt="Flowchart1" width="600"/>
  </kbd>
</p>

*Figure 1: Map of the research proposal. Created with Whimsical*

---

## **Table of Contents**
* [Overview](./README.md#Overview)
* [Repository Structure](./README.md#Repository-Structure)
* [Key Features](./README.md#Key-Features)
* [Datasets](./README.md#Datasets)
* [Applications](./README.md#Applications)
* [Getting Started](./README.md#Getting-Started)
* [Final Poster](./README.md#Final-Poster)
* [Demo Videos](./README.md#demo-video)
* [Contributing](./README.md#Contributing)
* [License](./README.md#License)
* [References](./README.md#References)
* [Statement of Intellectual and Professional Growth](./README.md#Statement-of-Intellectual-and-Professional-Growth)
* [Navigation Instructions](./README.md#Navigation-Instructions)

---

## **Overview**

---AAA

---

## **Repository Structure**

- **[`Data/`](Data/README.md)**: Contains the datasets used in the project, including:
  - **Global Breast-cancer Dataset**:Processed data from 5 countries.
- **[`Code/`](Code/READ.md)**: Python scripts for data preprocessing, integration, and visualization.
   - **`data_preprocessing.ipynb`**: Scripts for loading and aligning datasets.
   - **`visualization_tools.py`**: Functions for creating static and interactive visualizations.
   - **`machine_learning.ipynb`**: Includes machine learning pipelines and SHAP analysis.
   - **`/map`**: HTML file for the geospatial map that one can download and run on browser.
- **[`Discussions/`](Discussions/READ.md)**: Key insights, reflections, and future improvements based on project findings, the final poster, and peer evaluations.
- **[`Visualizations/`](Visualizations/README.md)**: Output visualizations and analysis results.
- **[`Docs/`](Docs/README.md)**: Supplementary documentation, final report.

---

## **Key Features**

- **Data Integration**:
  - Combines multiple datasets to explore misinformation across regions, platforms, and cultural contexts.
  - Aligns schemas for consistency and scalability in analysis.
- **Interactive Visualizations**:
  - Scatterplots for misinformation amplification patterns.
  - Network diagrams for dissemination pathways.
  - Choropleth maps for regional vulnerability analysis.

---

## **Datasets**

### **AAA**
- 

### **AA**
- 

---

## **Applications**

1. **AA**:
   - Identify misinformation hotspots and track the effectiveness of interventions.
   - Design culturally sensitive campaigns targeting misinformation-prone regions.

2. **AA**:
   - Tailor fact-checking strategies based on audience demographics.
   - Monitor and visualize the impact of fact-checking efforts.

3. **AA**:
   - Explore correlations between cultural factors and misinformation susceptibility.
   - Analyze temporal trends and the role of social context in misinformation acceptance.


---

## **Getting Started**

### **Prerequisites**
- Python 3.6 or higher
- Required libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `networkx`
  - `flask`
  - `shap`

### **Installation**
Clone the repository and install dependencies:

```bash
git clone https://github.com/AidaCPL/INFOSCI301_Final_Project.git
cd misinformation-visualization
pip install -r requirements.txt
```

### **Usage**
1. **Preprocess Data**:
   ```bash
   python scripts/data_preprocessing.ipynb
   ```
2. **Generate Visualizations**:
   ```bash
   python scripts/visualization_tools.py
   ```
---

## **Final Poster**
<p align="center">
  <kbd>
    <img src="INFORSCI 103 - Poster .png" alt="Final Poster" width="600"/>
  </kbd>
</p>

---

## **Demo Video**
VIDEO LINK IS HERE


---

## **Statement of Intellectual and Professional Growth**



---

## **Navigation Instructions**

This repository is organized to facilitate ease of access to all components of the project. Below is an overview of where to find key resources:

- **Code for Simulations, Data Processing, and Visualizations**:
  - Located in the [`Code/`](Code/README.md) directory.
  - Includes `data_preprocessing.ipynb` for cleaning and integrating datasets, and `visualization_tools.py` for generating the project’s visualizations.

- **Sample Datasets or Processed Data**:
  - Found in the [`Data/`](Data/README.md) folder.
  - Contains raw and processed datasets, including Climate-FEVER and the Global Misinformation Dataset.

- **Documentation for Dependencies and Environment Setup**:
  - Detailed in the [`Docs/`](Docs/README.md) directory.
  - Includes `requirements.txt` for library installation and a setup guide for running the visualizations.

- **Pilot Visualizations or Figures**:
  - Stored in the [`Visualizations/`](Visualizations/README.md) folder.
  - Features static and interactive outputs of the project’s key visualizations, including geospatial maps, network diagrams, and machine learning plots.

---

## **Contributing**
We welcome contributions to enhance the repository. Please submit issues or pull requests to suggest improvements or report bugs.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **References**
This project builds upon datasets and methodologies outlined in:
- aa
- aa
