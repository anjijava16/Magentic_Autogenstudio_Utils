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


### Flow 
1. Internally calling serve.py file

2. <img width="1728" alt="image" src="https://github.com/user-attachments/assets/c4c839f2-4e2f-41c8-8789-e372d97fffd0" />

```

import json
import os

from fastapi import FastAPI

from ..datamodel import Response
from ..teammanager import TeamManager

app = FastAPI()
team_file_path = os.environ.get("AUTOGENSTUDIO_TEAM_FILE", None)


if team_file_path:
    team_manager = TeamManager()
else:
    raise ValueError("Team file must be specified")


@app.get("/predict/{task}")
async def predict(task: str):
    response = Response(message="Task successfully completed", status=True, data=None)
    try:
        result_message = await team_manager.run(task=task, team_config=team_file_path)
        response.data = result_message
    except Exception as e:
        response.message = str(e)
        response.status = False
    return response


```


3. Calling team_manager.run (teammanager.py ) file

```
async def run(
        self,
        task: str,
        team_config: Union[str, Path, dict, ComponentModel],
        input_func: Optional[Callable] = None,
        cancellation_token: Optional[CancellationToken] = None,
    ) -> TeamResult:
        """Run team synchronously"""
        start_time = time.time()
        team = None

        try:
            team = await self._create_team(team_config, input_func)
            result = await team.run(task=task, cancellation_token=cancellation_token)

            return TeamResult(task_result=result, usage="", duration=time.time() - start_time)

        finally:
            # Ensure cleanup happens
            if team and hasattr(team, "_participants"):
                for agent in team._participants:
                    if hasattr(agent, "close"):
                        await agent.close()

```


# Autogenstudio end to end flow

![image](https://github.com/user-attachments/assets/32518bbc-7a14-4225-a053-5788fbf6d8e5)


