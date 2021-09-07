# rpa  
   
Python 3.9.6  
  
conda update conda  
conda create -n rpa python=3.9.6  
(conda create -n base -c rpa)  
conda install -c conda-forge numpy pandas  
conda info --envs  
conda install -c conda-forge jupyterlab pylint  
(magic comment : #%%)  
  
conda env export > rpa.yml  
conda env create -f rpa.yml  
  
