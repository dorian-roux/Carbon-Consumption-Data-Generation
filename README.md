<div align="center" style = "display: block; align-items: center;
  justify-content: center">
  <span align="center" style = "font-weight: 500; font-size: 20px;">ROULET Maria Paula & ROUX Dorian</span>  
  </br>
  <img src="./__Other/Images//CY TECH Logo.png" alt="Logo" height="80px" style = "margin: 10px">
  </br>
  <span align="center" style = "font-weight: 500; font-size: 18px;">4th Year International Bachelor in Data Science</span>  
</div>

## 1) About the Project

Develop a data generator capable of accurately depicting carbon consumption within an office setting and generate point-of-sale (POS) data. This project was conducted in collaboration with a startup aiming to enhance carbon consumption practices in office environments. The objective was to create a tool that could simulate and analyze carbon usage patterns within an office, providing valuable insights for the startup's initiatives to reduce carbon footprint and promote sustainability. Through the development of this data generator and the collection of POS data, the project sought to contribute to the startup's efforts in implementing effective strategies for carbon reduction and fostering environmentally conscious practices in workplace settings.

## 2) The Steps of the Project

### A) Research:
Conduct online research to gather datasets related to point-of-sale systems, carbon consumption through apps, or studies focusing on carbon footprint.

### B) POS:
Generate datasets for point-of-sale transactions across various industries (fashion, automotive, luxury) in different cities worldwide.

### C) App Footprint:
Compile a dataset detailing the carbon impact per minute (in grams of equivalent CO2 emissions) for various apps including newsfeeds, video conferencing platforms, and web browsers.

### D) CI Generator:
Develop a tool to generate carbon consumption data for each employee within a small office setting, on a minute-by-minute basis, over a defined period (3 to 6 months or a year).

## 3) Structure
```bash
.
├── Carbon_Impact
│   ├── CI_class.py
│   ├── Carbon-Impact_Generator.py
│   ├── Data
│   │   └── apps.csv
│   └── Exec_CI-class.py
├── Point of Sales
│   ├── Data
│   │   ├── SubData
│   │   │   ├── Car
│   │   │   │   ├── Renault
│   │   │   │   │   ├── pos_Renault.csv
│   │   │   │   │   ├── pos_Renault_11PoS.csv
│   │   │   │   │   ├── pos_Renault_16PoS.csv
│   │   │   │   │   ├── pos_Renault_31PoS.csv
│   │   │   │   │   ├── pos_Renault_51PoS.csv
│   │   │   │   │   └── pos_Renault_5PoS.csv
│   │   │   │   └── Volkswagen
│   │   │   │       ├── pos_Volkswagen.csv
│   │   │   │       ├── pos_Volkswagen_11PoS.csv
│   │   │   │       ├── pos_Volkswagen_16PoS.csv
│   │   │   │       ├── pos_Volkswagen_31PoS.csv
│   │   │   │       └── pos_Volkswagen_51PoS.csv
│   │   │   ├── Cosmetic
│   │   │   │   ├── MAC Cosmetics
│   │   │   │   │   ├── pos_MAC Cosmetics.csv
│   │   │   │   │   ├── pos_MAC Cosmetics_11PoS.csv
│   │   │   │   │   ├── pos_MAC Cosmetics_16PoS.csv
│   │   │   │   │   ├── pos_MAC Cosmetics_31PoS.csv
│   │   │   │   │   └── pos_MAC Cosmetics_51PoS.csv
│   │   │   │   └── Sephora
│   │   │   │       ├── pos_Sephora.csv
│   │   │   │       ├── pos_Sephora_11PoS.csv
│   │   │   │       ├── pos_Sephora_16PoS.csv
│   │   │   │       ├── pos_Sephora_31PoS.csv
│   │   │   │       └── pos_Sephora_51PoS.csv
│   │   │   ├── Luxury
│   │   │   │   ├── Cartier
│   │   │   │   │   ├── pos_Cartier.csv
│   │   │   │   │   ├── pos_Cartier_11PoS.csv
│   │   │   │   │   ├── pos_Cartier_16PoS.csv
│   │   │   │   │   ├── pos_Cartier_31PoS.csv
│   │   │   │   │   └── pos_Cartier_51PoS.csv
│   │   │   │   └── Prada
│   │   │   │       ├── pos_Prada.csv
│   │   │   │       ├── pos_Prada_11PoS.csv
│   │   │   │       ├── pos_Prada_16PoS.csv
│   │   │   │       ├── pos_Prada_31PoS.csv
│   │   │   │       └── pos_Prada_51PoS.csv
│   │   │   ├── Mode
│   │   │   │   ├── Nike
│   │   │   │   │   ├── pos_Nike.csv
│   │   │   │   │   ├── pos_Nike_11PoS.csv
│   │   │   │   │   ├── pos_Nike_16PoS.csv
│   │   │   │   │   ├── pos_Nike_31PoS.csv
│   │   │   │   │   └── pos_Nike_51PoS.csv
│   │   │   │   └── Zara
│   │   │   │       ├── pos_Zara.csv
│   │   │   │       ├── pos_Zara_11PoS.csv
│   │   │   │       ├── pos_Zara_16PoS.csv
│   │   │   │       ├── pos_Zara_31PoS.csv
│   │   │   │       └── pos_Zara_51PoS.csv
│   │   │   └── Tech
│   │   │       ├── Apple
│   │   │       │   ├── pos_Apple.csv
│   │   │       │   ├── pos_Apple_11PoS.csv
│   │   │       │   ├── pos_Apple_16PoS.csv
│   │   │       │   ├── pos_Apple_31PoS.csv
│   │   │       │   └── pos_Apple_51PoS.csv
│   │   │       └── Orange
│   │   │           ├── pos_Orange.csv
│   │   │           ├── pos_Orange_11PoS.csv
│   │   │           ├── pos_Orange_16PoS.csv
│   │   │           ├── pos_Orange_31PoS.csv
│   │   │           └── pos_Orange_51PoS.csv
│   │   ├── point_of_sale_db.csv
│   │   ├── pos_db.csv
│   │   └── worldcities.csv
│   ├── Exec_PoS-class.py
│   ├── PoS_class.py
│   └── Point-of-Sales_generator.py
├── README.md
├── _Notebooks
│   ├── Carbon Impact
│   │   ├── CI_Analysis.ipynb
│   │   └── CI_Generation.ipynb
│   └── Point of Sales
│       └── PoS_Generator.ipynb
└── __Other
    └── Images
        └── CY TECH Logo.png
```
