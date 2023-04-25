conda env remove -n "instalily_cc"
conda env create -n "instalily_cc" -f env_setup/instalily_cc.yml

## Install new environment.
python3 -m ipykernel install --user --name instalily_cc --display-name "Instalily Coding Challenge"
