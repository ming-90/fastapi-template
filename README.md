# Python Project Template
This repository is a python template repo for internal uses of Team project.

## File Structure
```bash
.
├── Makefile          # commands
├── README.md
├── requirements.txt  # package information
├── setup.cfg         # configurations for formatting & linting & unit-test
├ src
    ├── converter     # API 
        ├── test.py
```
## Prerequisities
1. Create conda env
```
$ make env
$ conda activate fastapi-template
$ make setup
```

1. Run the server
```
$ make run-server
```

<img width="491" alt="image" src="https://user-images.githubusercontent.com/48505409/200153152-91f64deb-adb3-417b-9885-2126f5259598.png">
