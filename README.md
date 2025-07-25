# [VOT]VideoCube VastTrack UAV20L TLP dataset for pytracking
在[pytracking](https://github.com/visionml/pytracking)中加入 [VideoCube(GIT)](http://videocube.aitestunion.com/index)[VastTrack](https://github.com/HengLan/VastTrack) [UAV20L](https://cemse.kaust.edu.sa/ivul/uav123) [TLP](https://amoudgl.github.io/tlp/) 数据集的测试和评估代码
## 使用方法
以[OSTrack](https://github.com/botaoye/OSTrack)为例
将项目中的py文件置于如下位置：
```
lib/test/evaluation/vasttrackdataset.py
lib/test/evaluation/uav20ldataset.py
lib/test/evaluation/tlpdataset.py
```
在同目录的datasets.py的对应位置添加：
```
vasttrack=DatasetInfo(module=pt % "vasttrack", class_name="VastTrackDataset", kwargs=dict())
tlp=DatasetInfo(module=pt % "tlp", class_name="TLPDataset", kwargs=dict()),
uav20l=DatasetInfo(module=pt % "uav20l", class_name="UAV20LDataset", kwargs=dict()),
```
## Test and evaluation
```
python tracking/test.py ostrack vitb_384_mae_ce_32x4_ep300 --dataset vasttrack --threads 16 --num_gpus 4
python tracking/test.py ostrack vitb_384_mae_ce_32x4_ep300 --dataset tlp --threads 16 --num_gpus 4
python tracking/test.py ostrack vitb_384_mae_ce_32x4_ep300 --dataset uav20l --threads 16 --num_gpus 4
python tracking/analysis_results.py # need to modify tracker configs and names
```
