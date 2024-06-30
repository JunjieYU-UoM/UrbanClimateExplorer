import ipywidgets as widgets
from IPython.display import display
import json
def get_text(k, v, type='Button'):
    """
    This function creates a text widget.
    
    Args:
        k: (str) The description of the text widget.
        v: (str) The value of the text widget.
    
    Returns:
        widgets.Text: A text widget.
    """
    if isinstance(v, (str, int, float)):
        return widgets.Text(
                value=v,
                placeholder='Type something',
                description=k,
                disabled=False,
                )
    elif isinstance(v, list):
        value = "".join(f"{str(item)}," for item in v).strip(',')
        return widgets.Textarea(
            value=value,
            placeholder='Enter list items, separated by commas',
            description=k,
            disabled=False
            )
    elif type == 'Button':
        return widgets.Button(description="submit")

button = widgets.Button(description="Submit")

def input_form(json_file="config_cesm1.json"):
    
    with open(json_file,'r') as f:
        data = json.load(f)
        layout = {}
        for key in data.keys():
            if isinstance(data[key], dict):
                for k in data[key].keys():
                    if isinstance(data[key][k], float):
                        layout[k] = {
                            'type': 'float',
                            'widget': get_text(k, str(data[key][k]))
                        }
        
            elif isinstance(data[key], list):
                layout[key] = {
                    'type': 'list',
                    'widget': get_text(key, data[key])
                }
                
            elif isinstance(data[key], (float)):
                layout[key] = {
                    'type': 'float',
                    'widget': get_text(key, str(data[key]))
                }
            elif isinstance(data[key], (int)):
                
                layout[key]={
                    'type': 'int',
                    'widget': get_text(key, str(data[key]))
                }
            else:
                layout[key] = {
                    'type': 'str',
                    'widget': get_text(key, data[key])
                }
                
    button = widgets.Button(description="Submit")

    def on_button_clicked(b):
        for key in layout.keys():
            if layout[key]['type'] == 'float':
                data[key] = float(layout[key]['widget'].value)
            elif layout[key]['type'] == 'list':
                data[key] = layout[key]['widget'].value.split(',')
            elif layout[key]['type'] == 'int':
                data[key] = int(layout[key]['widget'].value)
            else:
                data[key] = layout[key]['widget'].value
                
        with open("./temp.json", 'w') as f:
            json.dump(data, f)

    button.on_click(on_button_clicked)
    layout_list = [layout[key]['widget'] for key in layout.keys()]
    i = widgets.VBox(layout_list, layout=widgets.Layout(flex_flow='row wrap'))
    display(i)
    display(button)