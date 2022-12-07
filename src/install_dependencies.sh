echo "Attempting to install cmake package"
CMAKE="cmake"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $CMAKE|grep "install ok installed")
echo Checking for $CMAKE: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "No $CMAKE. Setting up $CMAKE."
  sudo apt-get --yes install $CMAKE
fi
echo "Attempting to install python3"
PYTHON3="python3"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $PYTHON3|grep "install ok installed")
echo Checking for $PYTHON3: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "No $PYTHON3. Setting up $PYTHON3."
  sudo apt-get --yes install $PYTHON3
fi

echo "Attempting to install python packages"
python3 -c "import notebook"
if [ $? = 1 ]; then
  echo "No notebook. Setting up notebook."
  pip install notebook
fi
python3 -c "import pybind11"
if [ $? = 1 ]; then
  echo "No pybind11. Setting up pybind11."
  pip install pybind11
fi
python3 -c "import numpy"
if [ $? = 1 ]; then
  echo "No numpy. Setting up numpy."
  pip install numpy
fi
python3 -c "import pandas"
if [ $? = 1 ]; then
  echo "No pandas. Setting up pandas."
  pip install pandas
fi
python3 -c "import matplotlib"
if [ $? = 1 ]; then
  echo "No matplotlib. Setting up matplotlib."
  pip install matplotlib
fi
python3 -c "import scipy"
if [ $? = 1 ]; then
  echo "No scipy. Setting up scipy."
  pip install scipy
fi
python3 -c "import networkx"
if [ $? = 1 ]; then
  echo "No networkx. Setting up networkx."
  pip install networkx
fi
python3 -c "import seaborn"
if [ $? = 1 ]; then
  echo "No seaborn. Setting up seaborn."
  pip install seaborn
fi
python3 -c "import import_ipynb"
if [ $? = 1 ]; then
  echo "No import_ipynb. Setting up import_ipynb."
  pip install import_ipynb
fi