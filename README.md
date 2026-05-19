# Weights

本仓库存放 YOLOv8 模型训练得到的权重文件及转换后的推理引擎。

## 文件说明

| 文件 | 说明 |
|------|------|
| `best.pt` | 训练最佳权重（PyTorch 格式） |
| `last.pt` | 最后一轮训练权重（PyTorch 格式） |
| `0727_3.pt` / `0728.pt` | 历史训练权重（PyTorch 格式） |
| `250706/0706.pt` | 2025年7月6日批次权重（PyTorch 格式） |
| `best.engine` | best.pt 转换的 TensorRT 引擎 |
| `0727_3.engine` / `0728.engine` | 对应 .pt 转换的 TensorRT 引擎 |
| `250706/0706.engine` | 对应 .pt 转换的 TensorRT 引擎 |
| `best.onnx` | ONNX 中间格式文件 |
| `convert.py` | .pt 转 .engine 的转换脚本 |

## .pt 与 .engine 的区别

### .pt (PyTorch 模型权重)

- **来源**：YOLOv8 训练完成后直接保存的模型文件
- **特点**：包含完整的模型结构和权重参数，可用 PyTorch 框架加载继续训练或推理
- **运行方式**：需要 Python + PyTorch + CUDA 环境
- **用途**：模型训练、微调、验证、导出

### .engine (TensorRT 推理引擎)

- **来源**：由 .pt 或 .onnx 通过 TensorRT 优化导出得到
- **特点**：经过层融合、量化、内存优化等操作，推理速度更快但不可再训练
- **运行方式**：需要 TensorRT 运行时，可用 C++ 或 Python 调用，适合部署到 Jetson 等嵌入式设备
- **用途**：生产环境部署、实时推理

### 转换流程

```
.pt (PyTorch)  →  .onnx (ONNX)  →  .engine (TensorRT)
```

使用 `convert.py` 可通过一行命令完成转换：

```python
from ultralytics import YOLO
model = YOLO('path/to/model.pt')
model.export(format="engine")
```

## 数据集

`yolov8data/datasets/` 目录下包含训练所用的数据集（80 张训练图 + 19 张验证图），标注格式为 YOLO 格式的 `.txt` 文件。
