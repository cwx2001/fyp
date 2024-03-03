###
# Directory
###
.
├── net/
│   ├── standard/
│   │   ├── notl_roundabout.net.xml
│   │   └── rltl_roundabout.net.xml
│   └── subang/
│       ├── subang_notl_roundabout.net.xml
│       └── subang_rltl_roundabout.net.xml
├── result/
│   ├── standard/
│   │   ├── biased/
│   │   │   ├── ma_norltl.png
│   │   │   ├── ma_notl.png
│   │   │   ├── ma_rltl.png
│   │   │   ├── norltl_biased_result.csv
│   │   │   ├── notl_biased_result.csv
│   │   │   └── rltl_biased_result.csv
│   │   ├── dense/
│   │   │   ├── ma_norltl.png
│   │   │   ├── ma_notl.png
│   │   │   ├── ma_rltl.png
│   │   │   ├── norltl_dense_result.csv
│   │   │   ├── notl_dense_result.csv
│   │   │   └── rltl_dense_result.csv
│   │   ├── normal/
│   │   │   ├── ma_norltl.png
│   │   │   ├── ma_notl.png
│   │   │   ├── ma_rltl.png
│   │   │   ├── norltl_normal_result.csv
│   │   │   ├── notl_normal_result.csv
│   │   │   └── rltl_normal_result.csv
│   │   ├── barh_biased.png
│   │   ├── barh_dense.png
│   │   └── barh_normal.png
│   └── subang/
│       ├── dense/
│       │   ├── ma_norltl_dense.png
│       │   ├── ma_notl_dense.png
│       │   ├── ma_notl_dense_zoom.png
│       │   ├── ma_rltl_dense.png
│       │   ├── norltl_dense_result.csv
│       │   ├── notl_dense_result.csv
│       │   └── rltl_dense_result.csv
│       ├── normal/
│       │   ├── ma_norltl.png
│       │   ├── ma_notl.png
│       │   ├── ma_rltl.png
│       │   ├── norltl_normal_result.csv
│       │   ├── notl_normal_result.csv
│       │   └── rltl_normal_result.csv
│       ├── barh_dense.png
│       └── barh_normal.png
├── routes/
│   ├── standard/
│   │   ├── weights/
│   │   │   ├── biased_weights.src.xml
│   │   │   ├── normal_weights.dst.xml
│   │   │   ├── normal_weights.src.xml
│   │   │   └── normal_weights.via.xml
│   │   ├── biased.rou.xml
│   │   ├── dense.rou.xml
│   │   └── normal.rou.xml
│   └── subang/
│       ├── subang_dense.rou.xml
│       └── subang_normal.rou.xml
├── scripts/
│   ├── tools/
│   │   ├── plot.py
│   │   └── randomTrips.py
│   ├── barh.py
│   ├── histogram.py
│   └── main.py
└── README.txt


###
# Contents
###
# net directory contains .xml files for traffic environments
# result directory contains .csv and .png files of simulation results
# routes directory contains .xml files for traffic demand elements
# scripts directory contains scripts used in the project. Tools directory includes the plot.py and randomTrips.py scripts which are provided by the SUMO-RL library and SUMO software respectively.

###
# Setting up (Windows 10)
###
1. install virtualenv with pip install virtualenv
2. CD to capstone_project2
3. run command $ Scripts\active
4. CD to simulator/scripts
5. run scripts of choice e.g. $ python main.py
5.run command $ deactivate
	to deactivate virtual environment


###
# Commands
###
# Command to run the randomTrips.py file:
python randomTrips.py -n <XML_FILE> -e <TOTAL_TIMESTEPS> --binomial <VEHICLE_SPAWN_AMOUNT> --fringe-factor <MAX> --period <FLOAT>

# Command to run the plot.py file:
python plot.py -f <CSV_FILE> -ma <FLOAT>
