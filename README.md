# Pothole Detection using YOLOv4
[![Docker Push](https://github.com/brianadit24/PotholeDetection/workflows/docker-build-push/badge.svg)](https://github.com/brianadit24/PotholeDetection/actions)

![Index_Result](results/result.jpeg)

## Introduction
This is API for Pothole Detection using Darknet YOLOv4.

## Tutorial

Clone the project

```bash
  git clone https://github.com/brianadit24/PotholeDetection
```

Go to the project directory

```bash
  cd PotholeDetection
```

Create and start API service

```bash
  docker-compose up
```

Stop and remove API service

```bash
  docker-compose down
```

  
## API Reference

Service: http://your-ip-address:8080

#### POST image

```http
  POST /predict
```
Content-Type: multipart/form-data
| Name    | Type   | Description                                         |
| :------ | :----- | :-------------------------------------------------- |
| `image` | `file` | **Required**. `image/jpeg` or `image/png` MIME Type |


## Result Example

**Input:**<br>
![Pothole1](results/test_1.jpg)

**Output:**<br>
![Pothole1_Result](results/test_result_1.jpeg)

---

**Input:**<br>
![Pothole2](results/test_2.jpg)

**Output:**<br>
![Pothole2_Result](results/test_result_2.jpeg)
 

  
