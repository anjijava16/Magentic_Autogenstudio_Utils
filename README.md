# Magentic_autogen

Autogen Magentic


https://github.com/microsoft/autogen/tree/v0.4.4/python/packages/autogen-magentic-one


https://github.com/microsoft/autogen/tree/main/python/packages/autogen-magentic-one



## Install

 1013  pip install "autogen-ext[magentic-one,openai]"

  cd autogen/python/packages/

 cd magentic-one-cli
 
 1018  ls -ltr
 
 1019  pip install -e .
 
 1020  playwright install --with-deps chromium



# Autogenstudio Installation
 
welcome@jaisairams-Laptop ~ % source ~/.zprofile.sh


welcome@jaisairams-Laptop ~ % conda create -n autogen_studio



welcome@jaisairams-Laptop ~ % source activate autogen_studio
(
autogen_studio) welcome@jaisairams-Laptop ~ % 



# # Install autogenstudio

pip install autogenstudio


## Run the Autogenstudion URL :

autogenstudio ui --port 8082 --appdir ./autogen_dir

<img width="1719" alt="image" src="https://github.com/user-attachments/assets/31f21803-ed47-44dc-842f-d448cbd98fde" />


## How to run autogen FastAPI UI using teamconfig.json


(autogen_studio) welcome@jaisairams-Laptop autogen_studio_config % pwd

/Users/welcome/Desktop/data/autogen_studio_config

(autogen_studio) welcome@jaisairams-Laptop autogen_studio_config % autogenstudio serve --team AssistantAgent_2_tool_config.json --port 8084

INFO:     Started server process [96066]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

INFO:     Uvicorn running on http://127.0.0.1:8084 (Press CTRL+C to quit)

INFO:     127.0.0.1:55913 - "GET /docs HTTP/1.1" 200 OK

INFO:     127.0.0.1:55913 - "GET /openapi.json HTTP/1.1" 200 OK

/Users/welcome/anaconda3/lib/python3.11/site-packages/autogen_core/_component_config.py:252: UserWarning: 
⚠️  SECURITY WARNING ⚠️
Loading a FunctionTool from config will execute code to import the provided global imports and and function code.
Only load configs from TRUSTED sources to prevent arbitrary code execution.
  instance = component_class._from_config(validated_config)  # type: ignore

INFO:     127.0.0.1:55916 - "GET /predict/What%20is%20AI HTTP/1.1" 200 OK

URL : http://localhost:8084/docs#/default/predict_predict__task__get


![image](https://github.com/user-attachments/assets/dec31bef-e198-4539-9cc6-6bda0a3d56c0)


