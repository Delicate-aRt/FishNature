I propose to store here label's files only and the real data should be provided by adding sim-link.

##### First step
Adding sim-link to the unpacked data. In my case that was:
```
$ cd DATA/
$ ln -s /mnt/STORAGE/DATA/TheNatureConservancy/unpacked/train_set train_set
```

##### Second step
Using *sloth* generate json file using relative path (so other can modify labels locally and to prevent future issues during merging all labels to one file):
```
$ cd DATA/train_set_labels
$ sloth appendfiles YFT.json ../train_set/YFT/*
```

This will create YFT.json using relative path e.g.:

```javascript
...
    {
        "annotations": [],
        "class": "image",
        "filename": "../train_set/YFT/img_07852.jpg"
    }
...
```

##### Third step
Run *sloth* using prepared config & generated file to start labeling:
```
$ cd DATA/train_set_labels
$ sloth --config ../../sloth_conf/sloth_cfg.py YFT.json
```

I guess everyone can work on each class separately and then all *.json files will be merged (if needed).

How we label:
* We are using squares only
* For NoF class - just put one point somewhere on the image
* We label: 
  * Fish itself 
  * Fish's head --- QUESTIONABLE. SHOULD WE DO THAT FOR SURE?
  * Fish's tail --- QUESTIONABLE. SHOULD WE DO THAT FOR SURE?

**PS**
In case we are labeling fish & head/tail and there are few fishes on screen - could be difficult to define which tail/head belongs to which fish.


