# 手順
Anacondaの仮想環境の作成、CUDAのtoolkitのインストール、Pytorchのインストールを行います。
## 仮想環境の作成

```
conda create -n First_MNIST python=3.11 -y
```
### 仮想環境のアクティベイト
これが終わったら仮想環境をアクティベイトします。絶対してください！
```
conda activate First_MNIST
```
これでいままで```(base)```となっていたものが```(First_MNIST)```となっているはずです。

絶対にそのようになっていることを確認してから次に進んでください。

### CUDA-Toolkitのインストール

```
conda install -c nvidia cuda-toolkit=12.1.0 -y
```
### Pytorchのインストール

```
conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia -y
```
### ここまでの確認

ここまで終わったら、Pytorch_Check.pyを実行します。
実行するとPytorchのバージョンやGPUや使用可能かどうか確認できます。

```
python Pytorch_Check.py
```
これで出力が次のようになっていればOKです。
```
2.3.1
Train on GPU: True
```

