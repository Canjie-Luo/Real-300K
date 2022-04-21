# Real-300K Dataset

- The dataset used in the CVPR'22 paper entitled "SimAN: Exploring Self-Supervised Representation Learning of Scene Text via Similarity-Aware Normalization." 
- It contains 293096 realistic and diverse scene text images collected from public real training datasets. 
- Check the [paper](https://arxiv.org/abs/2203.10492) for details.

## Download

- Download the dataset from [Google Drive](https://drive.google.com/file/d/1CwiXhGNooQ0IempluAWei-kvb9GHRCGQ/view?usp=sharing) or [Baidu Cloud](https://pan.baidu.com/s/1Kaaeyya8gNLeflT93Naq-A?pwd=u8qe) (Password: u8qe). 
- The MD5 value of 'Real-300K-DataBase.zip' should be 'c3c9a91498f547ee24af52b573fb47be'.
- Unzip the 'Real-300K-DataBase.zip' file.

```
|___Real-300K-DataBase
|       |___data.mdb
|       |___lock.mdb
|___lmdb_visual.py
|___requirements.txt
|___README.md
```

## Requirement 
Python==3.7

```
pip install -r requirements.txt
```

## Visualization

```
python3 lmdb_visual.py
```

Check the ''demo'' folder for details.

## Citation

```
@inproceedings{Luo2022SimAN,
  title={SimAN: Exploring Self-Supervised Representation Learning of Scene Text via Similarity-Aware Normalization},
  author={Luo, Canjie and Jin, Lianwen and Chen, Jingdong},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages={1--10},
  year={2022}
}
```
