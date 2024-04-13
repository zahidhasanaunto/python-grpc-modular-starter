# To run locally

#### Clone repo

```bash
$ git clone <repo>
```

#### Create virtual env

```bash
$ virtualenv env
```

#### Activate env

```bash
$ source env/bin/activate
```

#### Setup .env

```bash
$ cp .env.example .env
```

#### Install dependencies

```bash
$ pip install -r requirements.txt
```

#### Compile protobuf

```
$ python -m grpc_tools.protoc -I ./prototype --python_out=./src/shared/types --grpc_python_out=./src/shared/types ./prototype/*.proto
```

#### Run app

```
$ python main.py
```
