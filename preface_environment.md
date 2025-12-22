```Qiskit``` is the open-source software development kit(SDK) for working with quantunm computers from IBM.
It provide free Quantum Computing framework for quantum computing researchers to work and use.

To conduct the ```Qiskit```, we should use python as the fundenmental platform and jupyter notebook to conductor
each operators. If in Windows other than Linux, using anaconda is more convience.



First we should set up the virtual enviornment. Here are some useful anaconda prompt terminal commands.
check the conda version:

```conda --version```

(but it`s no need to update the conda version, because use the low version can still establish a high python version virtual enviornment)
list all the existed virtual enviornment:

```conda env list```

create new virtual enviornment:

```conda create -n qiskit-env python==3.11```

(for qiskit, it`s better use the newest python version > 3.10, because the quantum computing SDK is frequently updated and the low
version 3.9 is deprecated as of the 2.1.0 release, 3.8 is deprecated as of the 1.1.0 release. Support for running Qiskit with Python
below 3.10 will be removed)
change the enviornment from base to the virtual enviornment:

```conda activate qiskit-env```

exit the environment:

```conda deactivate```

delect the virtual environment:

```conda env remmove -n qiskit```



      
Second, we should install qiskit and relative package. we can use pip or conda to install
if we use pip, pip update:

```pip install pip -U```

install qiskit and other packages

```pip install qiskit[visualization] -U```

```pip install qiskit-ibm-runtime -U```

```pip install qiskit-ibm-provider[visualization] -U```

```pip install qiskit-aer -U```


those are the API references:

https://docs.quantum.ibm.com/api/qiskit
https://docs.quantum.ibm.com/api/qiskit-ibm-runtime
https://docs.quantum.ibm.com/api/qiskit-ibm-provider
https://qiskit.org/ecosystem/aer/index.html

User support:

https://quantumcomputing.stackexchange.com/




