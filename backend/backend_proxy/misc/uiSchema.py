
def createUiSchema(inputList):
    schema = {
        "title": "  Interactive Demo",
        "type": "object",   
        "properties": {
        
        }
    }
    uiSchema = {}
    for inputIndex in range(len(inputList)):
        schema["properties"][f"input_{inputIndex}"] = {
            "type": "string",
            "title": inputList[inputIndex]['data_type']
        }
        uiSchema[f"input_{inputIndex}"] = {
            "ui:widget": "textarea",
            "ui:emptyValue": inputList[inputIndex]['data_type']
        }

    return schema, uiSchema