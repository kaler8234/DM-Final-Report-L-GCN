## 資料集創建
1. 圖片篩選的方式如報告 PPT 所述
2. 創建 dataset 可使用 facenet 資料夾中 dataset_produce.py，過程中每個步驟有用分隔線隔開。
* 在做最後一步前請確認檔案依照以下格式放置圖片(0、1為class的編號)
```
.  
└─dataset  
    ├─0
    │   0.png
    |   1.png
    │   ...
    ├─1
    │   0.png
    |   1.png
    │   ...
    └─ ...
```
3. 在最後會產生已經過CNN特徵提取的.npy檔(label & feature)
   
## RUN L-GCN
* 在此步驟前如還沒有 knn 的資料檔請將 feature.npy 經過 L-GCN with RIWS 內的 tools/get_knn.py 處理後取其中的index檔案
* 此部分 train.py 與 test.py 在 L-GCN 資料夾內
#### Train Phase
在確認有 feature.npy、knn_data.npy、label.npy 檔案後可在 cmd 跑下述指令
```sh
python train.py --feat_path path/to/features --knn_graph_path path/to/knn/graph --labels_path path/to/labels
```

#### Test Phase
在確認有 feature.npy、knn_data.npy、label.npy 檔案後可在 cmd 跑下述指令
```sh
python test.py --val_feat_path path/to/features --val_knn_graph_path path/to/knn/graph --val_labels_path path/to/labels --checkpoint path/to/gcn_weights
```

## RUN L-GCN with RIWS
* 在此步驟前如還沒有 knn 的資料檔請將 feature.npy 經過 L-GCN with RIWS 內的 tools/get_knn.py 處理後取其中的 index 檔案

* 此部分 train.py 與 test.py 在 L-GCN with RIWS/imbalance_gcn 資料夾內

#### Train Phase

在確認有 feature.npy、knn_data.npy、label.npy 檔案後可在 cmd 跑下述指令

```sh
python train.py --feat_path path/to/features --knn_graph_path path/to/knn/graph --labels_path path/to/labels
```

#### Test Phase

在確認有 feature.npy、knn_data.npy、label.npy 檔案後可在 cmd 跑下述指令

```sh
python test.py --val_feat_path path/to/features --val_knn_graph_path path/to/knn/graph --val_labels_path path/to/labels --checkpoint path/to/gcn_weights
```

## 環境
上述所有步驟均是在 WSL Ubuntu 20.04.6 LTS 環境執行
Python 版本為 3.10.13
pip 安裝各套件版本如下
```
Brotli @ file:///tmp/abs_ecyw11_7ze/croots/recipe/brotli-split_1659616059936/work
certifi @ file:///croot/certifi_1700501669400/work/certifi
cffi @ file:///croot/cffi_1700254295673/work
charset-normalizer @ file:///tmp/build/80754af9/charset-normalizer_1630003229654/work
contourpy==1.2.0
cryptography @ file:///croot/cryptography_1694444244250/work
cycler==0.12.1
faiss==1.7.4
filelock @ file:///croot/filelock_1700591183607/work
fonttools==4.45.1
fsspec==2023.10.0
gmpy2 @ file:///tmp/build/80754af9/gmpy2_1645455533097/work
idna @ file:///croot/idna_1666125576474/work
Jinja2 @ file:///croot/jinja2_1666908132255/work
joblib==1.3.2
kiwisolver==1.4.5
MarkupSafe @ file:///opt/conda/conda-bld/markupsafe_1654597864307/work
matplotlib==3.8.2
mkl-fft==1.3.1
mkl-random @ file:///home/builder/ci_310/mkl_random_1641843545607/work
mkl-service==2.4.0
mpmath @ file:///croot/mpmath_1690848262763/work
networkx @ file:///croot/networkx_1690561992265/work
numpy @ file:///croot/numpy_and_numpy_base_1682520569166/work
opencv-python==4.8.1.78
packaging==23.2
Pillow @ file:///croot/pillow_1696580024257/work
pycparser @ file:///tmp/build/80754af9/pycparser_1636541352034/work
pyOpenSSL @ file:///croot/pyopenssl_1690223430423/work
pyparsing==3.1.1
PySocks @ file:///home/builder/ci_310/pysocks_1640793678128/work
python-dateutil==2.8.2
PyYAML @ file:///croot/pyyaml_1698096049011/work
requests @ file:///croot/requests_1690400202158/work
scikit-learn==1.3.2
scipy==1.11.4
six @ file:///tmp/build/80754af9/six_1644875935023/work
sympy @ file:///croot/sympy_1668202399572/work
threadpoolctl==3.2.0
torch==2.1.1
torchaudio==2.1.1
torchvision==0.16.1
tqdm==4.66.1
triton==2.1.0
typing_extensions @ file:///croot/typing_extensions_1690297465030/work
urllib3 @ file:///croot/urllib3_1698257533958/work
```
