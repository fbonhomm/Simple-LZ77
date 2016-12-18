
# Simple LZ77

implementing the algorithm Lempel–Ziv–77 in Python3

## Usage:

### setting.py
- the file setting is all option for compress

### compress.py
- python3 compress.py [original] [compressed]

### decompress.py
- python3 decompress.py [compressed] [decompressed]

### Graphic Interface
- python3 Interface/graphic.py

## Explication:
- window = size of window

## Benchmark:
Original Size   | Compressed - window[65536] |  Ratio  | Compressed - window[255] |  Ratio  |
--------------- | -------------------------- | ------- | ------------------------ | ------- |
     84 bytes   |           188 bytes        |+123.809%|             141 bytes    | +67.857%|
    598 bytes   |           612 bytes        |  +2.341%|             474 bytes    | -20.735%|
  22301 bytes   |          8720 bytes        | -60.898%|           11424 bytes    | -48.773%|
 285376 bytes   |         87624 bytes        | -69.295%|          195543 bytes    | -31.478%|

### Time:
Original Size   | Compressed - dict[65536], pos[16] | Compressed - dict[255], pos[8] |
--------------- | --------------------------------- | ------------------------------- |
 285376 bytes   |               95.38s              |             12.13s              |
