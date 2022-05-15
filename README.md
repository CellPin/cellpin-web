# CellPin
This application offer two functions. <br/>
    - classifies whether cells in the given image(X100 magnification) are CPE or No CPE. <br/>
    - calculates the TCID50 by entering the following variables.

## How to work (Click on image.)
[![CellPin 팀 웹페이지 시연영상](https://img.youtube.com/vi/yzHPEwOc6MA/0.jpg)](https://youtu.be/yzHPEwOc6MA&t=0s)

## How to install
1. Download the repository.
```
git clone https://github.com/CellPin.git
```

2. Install the Docker. <br/>
[docker installation](https://docs.docker.com/engine/install/)  <br/>
[nvidia docker installation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) (If you only want to get TCID50, you don't need to install this one.)

3. Download the weight file below. <br/>
Download https://drive.google.com/file/d/1DriLyB7HF9IYx_faGO0QCsNGzRNwZWNw/view?usp=sharing
and move into `CellpinWeb/models/` path.

4. Build a Docker file and Run a Docker image.
```
cd CellpinWeb
sudo docker build -t cellpin:latest . 
sudo docker run -p 80:80 cellpin:latest (If you only want to get TCID50 ...)
sudo docker run --gpus '"device=0"' -p 80:80 cellpin:latest (Depending on the number of GPU units, you can add device numbers.)
```

5. Check your browser <br/>
Type 127.0.0.1:80 into your browser.


## Contribution
CellPin Team building
1. [Hyeseong Lee](https://github.com/orgs/CellPin/people/gotjd709)
    - Main: DataLabeling, DataPreprocessing
2. [Donghun lee](https://github.com/orgs/CellPin/people/Soah-1994)
    - Main: ModelArchitecture, Sub: TCID50Calculator
3. [Kipyo Ryu](https://github.com/orgs/CellPin/people/fbrlvy87)
    - Main: Augmentation, TCID50Calculator, Sub: ModelArchitecture
4. [Jonghoon Park](https://github.com/orgs/CellPin/people/Zion-J-Park)
    - Main: BackEnd
5. [Jeongwoo Kim](https://github.com/orgs/CellPin/people/mochafreddo)
    - Sub: BackEnd

## Acknowledgement
Data Contribution: Virology Lab(Hye Kwon Kim, D.V.M., Ph. D. Assistant Professor), Department of Microbiology, College of Natural Science, Chungbuk National University

## Reference
- Wang, Ting-En et al. “Differentiation of Cytopathic Effects (CPE) induced by influenza virus infection using deep Convolutional Neural Networks (CNN).” PLoS computational biology vol. 16,5 e1007883. 13 May. 2020, doi:10.1371/journal.pcbi.1007883
