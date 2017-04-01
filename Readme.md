# Bokeh integration into Apache Zeppelin

(http://bokeh.pydata.org) 

## Approach

Bokeh global state management depends on a global variable which is sufficient if there is a 1-to-1 relationship between a notebook and a kernel as with IPython/Jupyter. 

Zeppelin will have multiple notebooks for each interpreter, hence Bokeh state management needs to be enhanced to support a state per Zeppelin Notebook (else `push_notebook` will fail when more than one tab with notebooks and Bokeh plots are open). 

BokehStates will wrap the global Bokeh state per Zeppelin notebook and is only necessary if you plan to have more than one Zeppelin tab in the browser using Bokeh.

## Preparation

To sue Bokeh, you first need to initiate the zeppelinCommLayer (details see [https://github.com/bernhard-42/zeppelin-ipython-shim](https://github.com/bernhard-42/zeppelin-ipython-shim))

```python
%pyspark

from zeppelin_comm_layer import ZeppelinCommLayer, resetZeppelinCommLayer

resetZeppelinCommLayer(z.z)

zcl = ZeppelinCommLayer(z.z)
```

In the next Paragraph start the shim (note: this cannot be done in the paragraph above)

```python
zcl.start()
```

Finally wrap the Bokeh globa state for the current notebook

```python
%pyspark

from zeppelin_bokeh import BokehStates

BokehStates(z.z).initState()
```

Now you can use Bokeh in Apache Zeppelin as in Jupyter Notebook


## License

Copyright 2017 Bernhard Walter

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.