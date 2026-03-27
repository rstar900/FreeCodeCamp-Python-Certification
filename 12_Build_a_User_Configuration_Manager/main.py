def add_setting(settings_dict, kv_tuple):
    key, value = kv_tuple
    # Convert key and value to lowercase
    key = key.lower()
    value = value.lower()
    # Key-Value validation
    if key in settings_dict.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    # Add key-value pair to settings dictionary    
    else:
        settings_dict.update({key:value})
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, kv_tuple):
    key, value = kv_tuple
    # Convert key and value to lowercase
    key = key.lower()
    value = value.lower()
    # Key-Value validation
    if not (key in settings_dict.keys()):
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    # Update value in settings dictionary    
    else:
        settings_dict.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings_dict, key):
    # Convert key and value to lowercase
    key = key.lower()
    # Key-Value validation
    if not (key in settings_dict.keys()):
        return "Setting not found!"
    # Delete key-value pair in settings dictionary    
    else:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"

def view_settings(settings_dict):
    # Empty Dictionary
    if len(settings_dict.keys()) == 0:
        return 'No settings available.'
    #Print the dictionary    
    else:
        formatted_settings_dict_string = ''
        for key, value in settings_dict.items():
           formatted_settings_dict_string += key.capitalize() + ': ' + value + '\n' 
        return 'Current User Settings:\n' + formatted_settings_dict_string    

test_settings = {'setting': 'value'}
